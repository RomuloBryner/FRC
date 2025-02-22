#!/usr/bin/env python3
import wpilib
import wpilib.drive
from wpilib import SmartDashboard
from wpilib import PowerDistribution, DigitalInput
from phoenix5 import WPI_VictorSPX
from wpilib.drive import DifferentialDrive

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Initializes the robot's components"""
        self.timer = wpilib.Timer()

        # Motor Controllers - Talons
        self._initMotors()

        # Speed Limit
        self.speed_limit = 0.7

        # Elevator Motors
        self._initElevatorMotors()

        # Elevator limit switches
        self._initElevatorSwitches()

        # Joystick controller
        self.joystick = wpilib.XboxController(0)

        # Power Distribution Panel (PDP)
        self.pdp = PowerDistribution(0, wpilib.PowerDistribution.ModuleType.kCTRE)

        # Variable to track the current elevator level
        self.current_elevator_level = None  # None means the elevator hasn't been moved to any level yet

    def _initMotors(self):
        """Initialize the drive motors and followers"""
        self.talonLeft = WPI_VictorSPX(3)
        self.talonLeft_follower = WPI_VictorSPX(1)
        self.talonRight = WPI_VictorSPX(4)
        self.talonRight_follower = WPI_VictorSPX(2)

        self.talonLeft_follower.follow(self.talonLeft)
        self.talonRight_follower.follow(self.talonRight)

        # Inversion setup
        self.talonLeft.setInverted(False)
        self.talonLeft_follower.setInverted(False)
        self.talonRight.setInverted(True)
        self.talonRight_follower.setInverted(True)

        # Robot Drive system
        self.drive = DifferentialDrive(self.talonLeft, self.talonRight)

    def _initElevatorMotors(self):
        """Initialize the elevator motors"""
        self.elevatorLeft = WPI_VictorSPX(5)
        self.elevatorRight = WPI_VictorSPX(6)
        self.elvatorDrive = DifferentialDrive(self.elevatorLeft, self.elevatorRight)

    def _initElevatorSwitches(self):
        """Initialize limit switches for the elevator"""
        self.switch_level_1 = DigitalInput(7)  # Limit switch for level 1
        self.switch_level_2 = DigitalInput(8)  # Limit switch for level 2
        self.switch_level_3 = DigitalInput(9)  # Limit switch for level 3

    def autonomousInit(self):
        """Called once when autonomous mode starts"""
        self.timer.restart()

    def autonomousPeriodic(self):
        """Called periodically during autonomous"""
        pass

    def teleopInit(self):
        """Called once when teleop mode starts"""
        pass

    def teleopPeriodic(self):
        """Called periodically during teleop mode"""
        self._updateSystemData()
        self._driveRobot()
        # self._operateElevator()
        self._manualElevatorControl()

    def _updateSystemData(self):
        """Update and display system data on the SmartDashboard"""
        system_voltage = self.pdp.getVoltage()
        system_current = self.pdp.getTotalCurrent()
        motor_current = self.pdp.getCurrent(12)
        
        SmartDashboard.putNumber("Robot Voltage", system_voltage)
        SmartDashboard.putNumber("Robot Current", system_current)
        SmartDashboard.putNumber("Robot Motor Current", motor_current)

        self._displayBatteryStatus(system_voltage)

    def _displayBatteryStatus(self, voltage):
        """Display battery status on the SmartDashboard"""
        if voltage > 13:
            SmartDashboard.putString("Battery State", "Good")
        elif 12 < voltage <= 13:
            SmartDashboard.putString("Battery State", "Caution")
        else:
            SmartDashboard.putString("Battery State", "Critical")

    def _driveRobot(self):
        """Drive the robot based on joystick input"""
        speed = self.speed_limit * -self.joystick.getLeftY()
        rotation = self.speed_limit * -self.joystick.getLeftX()
        self.drive.arcadeDrive(speed, rotation)

    def _operateElevator(self):
        """Control elevator movement with joystick input and limit switches"""
        if self.joystick.getAButtonPressed():  # Button A: Move to Level 1
            self.moveElevatorToLevel(0)
        elif self.joystick.getBButtonPressed():  # Button B: Move to Level 2
            self.moveElevatorToLevel(1)
        elif self.joystick.getXButtonPressed():  # Button X: Move to Level 3
            self.moveElevatorToLevel(2)

    def moveElevatorToLevel(self, target_level):
        """Move the elevator to the specified target level using limit switches"""
        # Prevent unnecessary movement if the elevator is already at the target level
        if self.current_elevator_level == target_level:
            print(f"Elevator is already at Level {target_level + 1}, no movement required.")
            return

        if target_level == 0:  # Move to Level 1 (bottom)
            self._moveElevatorToPosition(self.switch_level_1, -0.5, 0)
        elif target_level == 1:  # Move to Level 2 (middle)
            self._moveElevatorToPosition(self.switch_level_2, 0.5, 1)
        elif target_level == 2:  # Move to Level 3 (top)
            self._moveElevatorToPosition(self.switch_level_3, 0.6, 2)

        # Update the current elevator level once it has moved
        self.current_elevator_level = target_level

    def _moveElevatorToPosition(self, limit_switch, speed, target_level):
        """Move the elevator towards a target position and stop when reaching the limit switch"""
        print(f"Moving elevator to Level {target_level + 1} with speed {speed}")
        while not limit_switch.get():  # Continue moving until the limit switch is pressed
            self.elvatorDrive.arcadeDrive(speed, 0)  # Move elevator up or down
        self.elvatorDrive.arcadeDrive(0, 0)  # Stop the elevator when limit switch is pressed
        print(f"Elevator reached Level {target_level + 1}")

    def _manualElevatorControl(self):
        """Manually control the elevator with the joystick (fine-tuning)"""
        manual_speed = -(self.joystick.getRightY() * 0.7)
        if (self.switch_level_2.get() == False):
            manual_speed = 0
            print("Pressing...")
        self.elvatorDrive.arcadeDrive(manual_speed, 0)

    def testInit(self):
        """Called once when test mode starts"""
        pass

    def testPeriodic(self):
        """Called periodically during test mode"""
        pass

if __name__ == "__main__":
    wpilib.run(MyRobot)

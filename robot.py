#!/usr/bin/env python3
#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.about:blank#blocked
#

import wpilib
import wpilib.drive
from wpimath.geometry import Pose2d, Rotation2d
import math

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        # Asignacion de motores
        leftMotor = wpilib.PWMSparkMax(0)
        rightMotor = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.drive.DifferentialDrive(leftMotor, rightMotor)

        # Designación de Control Remoto
        self.driverController = wpilib.XboxController(0)

        # Campo 2D de la simulacion
        self.field = wpilib.Field2d()

        # Posición inicial del robot
        self.robotPos = [0, 0]
        # Rotación inicial del robot
        self.robotRotation = 1.457685

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        rightMotor.setInverted(True)
        
        # Exportar al campo 2D
        wpilib.SmartDashboard.putData("Field", self.field)
    

    def teleopPeriodic(self):
        """ Metodo para controlar el robot Teleoperadamente """

        # Asegurar que haya movimiento de los JS
        if(-self.driverController.getLeftY() > 0.5 or -self.driverController.getLeftX() > 0.5 or -self.driverController.getLeftY() < -0.5 or -self.driverController.getLeftX() < -0.5 or -self.driverController.getRightX() > 0.5 or -self.driverController.getRightX() < -0.5):
            
            # Obtener Posicion y Rotacion de los JS
            forward = -self.driverController.getLeftY() * 0.05
            rotation = -self.driverController.getRightX() * 0.05

            # Actualizar Rotacion del Robot
            self.robotRotation += rotation

            # Calcular la nueva Posicion del Robot con la Rotacion utilizando la libreria math
            deltaX = forward * math.cos(self.robotRotation)
            deltaY = forward * math.sin(self.robotRotation)
            
            # Asignar las posiciones al Robot
            self.robotPos[0] += deltaX
            self.robotPos[1] += deltaY

            # Actualizar las posiciones en la Simulacion
            self.field.setRobotPose(Pose2d(self.robotPos[0], self.robotPos[1], Rotation2d(self.robotRotation)))

            print(f"Robot Position: {self.robotPos}, Rotation: {self.robotRotation}")

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.restart()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            # Drive forwards half speed, make sure to turn input squaring off
            self.robotDrive.arcadeDrive(0.5, 0, squareInputs=False)
        else:
            self.robotDrive.stopMotor()  # Stop robot

    def teleopInit(self):
        """This function is called once each time the robot enters teleoperated mode."""

    def testInit(self):
        """This function is called once each time the robot enters test mode."""

    def testPeriodic(self):
        """This function is called periodically during test mode."""


if __name__ == "__main__":
    wpilib.run(MyRobot)
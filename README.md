# FRC
**First Robotics Competition project**

README FOR INSTALLATIONS

1. Instalaciones necesarias:
    VSCode - Entorno para programar el robot
        https://code.visualstudio.com/docs/?dv=win
    Python - lenguaje de programación a utilizar
        --WINDOWS--
            64-bit: https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe
            32-bit: https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe
        --MAC--
            https://www.python.org/ftp/python/3.12.0/python-3.12.0-macos11.pkg
    AdvantageScope - Para vista 3D de la simulación
        https://github.com/Mechanical-Advantage/AdvantageScope/releases/tag/v3.2.1

2. Librerias necesarias:
    RobotPy
        --WINDOWS--
            Run the following command from cmd or Powershell to install the core RobotPy packages:

            py -3 -m pip install robotpy
            To upgrade, you can run this:

            py -3 -m pip install --upgrade robotpy

            If you don’t have administrative rights on your computer, either use virtualenv/virtualenvwrapper-win, or or you can install to the user site-packages directory:

            py -3 -m pip install --user robotpy
        
        --MAC--
            On a macOS system that has pip installed, just run the following command from the Terminal application (may require admin rights):

            python3 -m pip install robotpy
            To upgrade, you can run this:

            python3 -m pip install --upgrade robotpy
            If you don’t have administrative rights on your computer, either use virtualenv/virtualenvwrapper, or you can install to the user site-packages directory:

            python3 -m pip install --user robotpy
    
    


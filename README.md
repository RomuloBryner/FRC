![🤖_First_Robotics_Competition 🤖](https://github.com/user-attachments/assets/39f5a98f-c73c-4e32-a243-6d8547711742)
# FRC: Proyecto de la Competencia First Robotics

Este proyecto utiliza Python, RobotPy y WPILib para programar y simular robots en el marco de la competencia **First Robotics Competition**. A continuación, se detallan las instrucciones de instalación y configuración necesarias para empezar.

---

#### 1. Instalaciones necesarias:

- ##### [Visual Studio Code (VSCode)](https://code.visualstudio.com/docs/?dv=win) - Entorno de desarrollo integrado (IDE) recomendado para programar el robot.
  
- ##### Python - Lenguaje de programación utilizado.
  - ###### [Windows (64-bit)](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)
  - ###### [Windows (32-bit)](https://www.python.org/ftp/python/3.12.0/python-3.12.0.exe)
  - ###### [MacOS](https://www.python.org/ftp/python/3.12.0/python-3.12.0-macos11.pkg)

- ##### [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope/releases/tag/v3.2.1) - Herramienta para visualizar la simulación del robot en 3D.

- ##### [WPILib](https://docs.wpilib.org/en/stable/docs/zero-to-robot/wpilib-setup.html) - Conjunto de herramientas y bibliotecas para programar y desplegar el código del robot en la competencia FRC.

---

#### 2. Librerías necesarias:

- ##### RobotPy  
    - **Instalación en Windows**  
      Abre `cmd` o `Powershell` y ejecuta el siguiente comando para instalar los paquetes principales de RobotPy:
      ```sh
      py -3 -m pip install robotpy
      ```
      Para actualizar RobotPy, usa:
      ```sh
      py -3 -m pip install --upgrade robotpy
      ```
      Si no tienes permisos de administrador en tu equipo, puedes usar un entorno virtual con `virtualenv/virtualenvwrapper-win` o instalarlo en el directorio de paquetes del usuario:
      ```sh
      py -3 -m pip install --user robotpy
      ```

    - **Instalación en MacOS**  
      Abre la aplicación Terminal y ejecuta el siguiente comando (puede requerir permisos de administrador):
      ```sh
      python3 -m pip install robotpy
      ```
      Para actualizar RobotPy, usa:
      ```sh
      python3 -m pip install --upgrade robotpy
      ```
      Si no tienes permisos de administrador, puedes usar `virtualenv/virtualenvwrapper` o instalarlo en el directorio de paquetes del usuario:
      ```sh
      python3 -m pip install --user robotpy
      ```

---

- **Documentación oficial:** Familiarízate con la [documentación oficial de WPILib](https://docs.wpilib.org/en/stable/) y [RobotPy](https://robotpy.readthedocs.io/en/stable/) para obtener detalles completos sobre las funciones disponibles y buenas prácticas para la programación del robot.

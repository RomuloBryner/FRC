![🤖_First_Robotics_Competition 🤖](https://github.com/user-attachments/assets/39f5a98f-c73c-4e32-a243-6d8547711742)

# FRC: Proyecto de la Competencia First Robotics

Este proyecto utiliza Python, RobotPy y WPILib para programar y simular robots en el marco de la competencia **First Robotics Competition**. A continuación, se detallan las instrucciones de instalación y configuración necesarias para empezar.

---

#### 1. Instalaciones necesarias:

- ##### [Visual Studio Code (VSCode)](https://code.visualstudio.com/docs/?dv=win) - Entorno de desarrollo integrado (IDE) recomendado para programar el robot.
- ##### [WPILib](https://docs.wpilib.org/en/stable/docs/zero-to-robot/step-2/wpilib-setup.html) - Instala Visual Studio Code con la libreria y herramientas de WPILib.
- ##### Python [Windows (64-bit)](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe) | [MacOS](https://www.python.org/ftp/python/3.12.0/python-3.12.0-macos11.pkg) - Lenguaje de programación utilizado.
- ##### [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope/releases/tag/v3.2.1) - Herramienta para visualizar la simulación del robot en 3D.

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

#### 3. Correr la simulacion:

  En la terminal, deben correr el siguiente comando para poder la simulación 2d.
    ```sh
    py -3 -m robotpy sim
    ```

  Para correr la simulación en 3d, se necesita tener abierta la simulacion 2d y tener instalado [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope/releases/tag/v3.2.1).

  Abren [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope/releases/tag/v3.2.1) y seleccionamos file:

  ![image](https://github.com/user-attachments/assets/aa5e583f-3958-4ae7-8d0e-36e5825a87a0)

  Luego, seleccionamos "Connect to Simulator"

  ![image](https://github.com/user-attachments/assets/a7b0c565-813c-490a-ab5f-b64c5f88412d)

 En la ezquina superior derecha, tenemos un signo de más, donde buscaremos "3D Field"

 ![image](https://github.com/user-attachments/assets/c73172ae-0747-4f05-a859-c1fde1747986)

 En el panel izquierdo se verá el Robot, tenemos que arrastrarlo al campo "3D Poses"

 ![image](https://github.com/user-attachments/assets/34dd0b63-d87c-4cee-9d7c-899c492bba71)

Aqui ya tendremos nuestro robot en la simulacion 3D

![image](https://github.com/user-attachments/assets/bb8bafd5-005b-4be5-88ef-d9f45c559b89)


---

- **Documentación oficial:** Familiarízate con la [documentación oficial de WPILib](https://docs.wpilib.org/en/stable/) y [RobotPy](https://robotpy.readthedocs.io/en/stable/) para obtener detalles completos sobre las funciones disponibles y buenas prácticas para la programación del robot.

## **README**

### **Vehicle Control Unit for Electric Vehicle**

**Final Year Mechatronics Engineering Project**

**Authors:** Mr. Prathmesh Barapatre, Mr. Rohit Acharekar, Mr. Tejas Panchal, Ms. Anupreeti Mahadik

This repository contains Python code for a Vehicle Control Unit (VCU) developed as a final year project. The VCU is built on a Flask RESTful API and renders HTML and CSS for a web-based interface that displays vehicle parameters.

**Key Features:**

* **Sensor Data Display:** Displays real-time sensor data such as odometer readings and other relevant metrics.
* **Data Storage:** Stores sensor data in a database for future analysis and visualization.
* **Geo-Fencing:** Defines virtual boundaries and triggers alerts when the vehicle enters or exits these boundaries.
* **Geo-Tracking:** Tracks the vehicle's location using GPS data.
* **Motor Control:** Allows for starting and stopping the vehicle's motor remotely from the web interface.

**Technologies:**

* **Python:** Programming language for the backend API and web development.
* **Flask:** Python web framework for building the RESTful API.
* **HTML/CSS:** Used for creating the web interface.
* **Database:** A suitable database (e.g., MySQL, PostgreSQL) for storing sensor data.
* **Hardware:** Sensors, microcontroller (if applicable), and communication modules for interfacing with the vehicle.

**Usage:**

1. **Set Up Environment:** Ensure you have Python 3.x and the required libraries (Flask, SQLAlchemy, etc.) installed.
2. **Configure Database:** Create a database and configure the connection details in the code.
3. **Implement Sensor Integration:** Integrate the necessary sensors and communication modules to gather vehicle data.
4. **Run the Flask App:** Start the Flask application to serve the web interface and API endpoints.

**Future Enhancements:**

* **Advanced Analytics:** Implement data analysis techniques to extract insights from the stored sensor data.
* **Remote Diagnostics:** Enable remote diagnostics and troubleshooting of vehicle issues.
* **User Authentication:** Add user authentication and authorization for secure access to the VCU.
* **Integration with Other Systems:** Integrate with other vehicle systems (e.g., battery management, charging) for comprehensive control.

**Contributions:**

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

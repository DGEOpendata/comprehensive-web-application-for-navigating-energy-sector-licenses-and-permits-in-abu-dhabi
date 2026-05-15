markdown
# Comprehensive Web Application for Navigating Energy Sector Licenses and Permits in Abu Dhabi

## Overview
This web application provides a centralized platform to access and interact with the 'Licenses and Permits in the Energy Sector 2025' dataset. Users can search for specific licenses, filter them by type or issuing authority, and download the data in user-friendly formats such as CSV or JSON.

## Features
- **Search Functionality:** Easily find specific licenses using keywords.
- **Downloadable Formats:** Download license data in CSV or JSON formats for further analysis.
- **Interactive Interface:** Navigate through licenses and permits using a user-friendly web interface.
- **Real-time Updates:** Get notified about new datasets or policy updates.
- **Educational Resources:** Access tutorials and webinars to learn how to use the dataset effectively.

## Prerequisites
- Python 3.9+
- Flask
- Pandas

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/YourUsername/EnergyLicensesPortal.git
   cd EnergyLicensesPortal
   
2. Install dependencies:
   bash
   pip install flask pandas
   
3. Place the `License_Categories.csv` in the root directory of the project.
4. Run the application:
   bash
   python app.py
   
5. Open your browser and navigate to `http://127.0.0.1:5000`.

## API Endpoints
### Search
- **Endpoint:** `/search`
- **Parameters:**
  - `query`: The keyword to search for in the dataset.
- **Method:** GET
- **Response:** JSON object containing filtered licenses.

### Download
- **Endpoint:** `/download/<format>`
- **Parameters:**
  - `format`: Format of the download file (`csv` or `json`).
- **Method:** GET
- **Response:** Downloadable dataset in the specified format.

## Contributing
To contribute, please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

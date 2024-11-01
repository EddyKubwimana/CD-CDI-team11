# Team Portfolio Landing Page with CI/CD

## Overview

This project is a collaborative effort by **Eddy**, **Tinotenda**, **Nicholas**, and **Candace** to create a **landing page** using Flask that links to each team member's individual portfolio. The primary goal is to showcase our understanding of Continuous Integration (CI) and Continuous Deployment (CD) by automating the build, testing, and deployment process for this project.

The landing page will feature links to each team member's portfolio and provide a streamlined way to view our skills and projects.

## Objectives

1. **Create a Team Landing Page**: Design a centralized page using Flask to feature each team member's name, role, and a link to their portfolio.
2. **Implement CI/CD**: Set up a CI/CD pipeline to automate the build, testing, and deployment of the Flask app.
3. **Individual Portfolios**: Each team member will have a basic portfolio to display their skills, experience, and projects.

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Version Control**: Git and GitHub
- **CI/CD Tool**: GitHub Actions for automated testing and deployment
- **Deployment Platform**: A cloud platform (GCP/AWS/Azure) content.

## Features

- **Landing Page**: A central Flask-powered page with links to each team member's individual portfolio.
- **Individual Portfolios**: Responsive, personal portfolio pages for Eddy, Tinotenda, Nicholas, and Candace.
- **Automated Deployment**: CI/CD workflow to automatically test and deploy changes to the landing page and individual portfolios.

## Project Structure

```plaintext
.
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   └── routes.py
├── .github/workflows/
│   └── ci-cd.yml
├── README.md
└── run.py

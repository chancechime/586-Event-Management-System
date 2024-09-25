# COMP 586 - Group Project 8

**Group Members:** Jack Konyan, Chance Chime, Luis Olmos

## Project Scope

**Event Registration Management System**

We aim to create a user-friendly event registration system that simplifies ticket purchasing and registration while generating QR codes for entry and providing administrative tools for event management. This project addresses frustrations with existing systems that often lead to long waits and service crashes.

## User Interface

The intuitive UI will allow users to navigate event listings, purchase tickets, and retrieve QR codes easily. Administrators will have access to user management and event oversight through a clear dashboard.

### Deliverables:

- **User Profile:**
  - Username
  - Encrypted Password
  - Tickets Purchased
  - Events Registered
  - Last Login
  - Reseller Status
  - First and Last Name
  - Admin Status

- **Event Details:**
  - Event Name
  - Event Description
  - Venue
  - Capacity
  - Tickets for Sale
  - Standing and Seated Tickets

## Data Management

Event details and user profiles, including ticket purchases and event registrations, will be securely stored and monitored.

## Assets

Key resources include:
- **QR Codes** for each ticket.
- **Event Assets** like banners and seating maps.
- **Live Ticket Data** for real-time availability.
- **User Data** for secure storage and monitoring.

## Networking/Cloud Service

We will use cloud services (e.g., Firebase) for real-time updates on ticket availability and user management.

## Mechanics and Rules

Core functions include ticket purchasing, QR code generation, user registration, and user management. Administrators can monitor activity and remove flagged users.

## Implementation

The system will be built using Flask for the back-end, with a cloud database for user and event data. The front-end will utilize HTML & Flask for a responsive experience, incorporating APIs for QR code generation.

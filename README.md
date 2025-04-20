Check out the interactive dashboard [here]([https://your-dashboard-link.com](https://web-chat.global.assistant.watson.appdomain.cloud/preview.html?backgroundImageURL=https%3A%2F%2Fau-syd.assistant.watson.cloud.ibm.com%2Fpublic%2Fimages%2Fupx-73ea27ea-633a-41a7-a617-b681a7293dcd%3A%3A0344fd36-6663-4470-8707-83b249f186a1&integrationID=0b2ffeee-c52f-4298-a5ec-e5509c695336&region=au-syd&serviceInstanceID=73ea27ea-633a-41a7-a617-b681a7293dcd))

# Singapore Tourism Chatbot 🌏
### This repository contains the Singapore Tourism Chatbot, designed to make your travel planning experience easier. The bot provides detailed information about Singapore, including travel itineraries, visa details, hotel bookings, and much more. It’s your one-stop solution for planning a trip to Singapore!

## Overview
### This chatbot is specialized in Singapore tourism, offering tailored responses for user queries related to the country’s culture, food, travel details, and more. It also provides interactive features like currency conversion, booking management, and live agent assistance.

## Key Features
### Primary Capabilities
- Friendly Greetings and Farewells
- Offers welcoming messages and polite goodbyes.

### General Information and Visa Details

- Answers questions about Singapore’s culture, food, weather, and visa application requirements.

### Itinerary Planning
- Helps create customized itineraries for group tours, including hotels and attractions.

### Tour and Hotel Bookings
- Allows users to book tourist attractions or hotels of their choice.

### Visa Application Assistance

- Collects necessary details for a simplified visa application process.

### Flight Booking Assistance
- Redirects users to flight booking websites if required.

### Error Handling for Non-Singapore Queries
- Responds appropriately when asked about other countries.

### Feedback Collection
- Gathers user feedback on the chatbot experience and services.

### Appointment Booking
- Schedules meetings for in-person or on-call consultations.

### Currency Conversion
- Converts foreign currencies to SGD (Singapore Dollars) and vice versa.

### Manage Bookings
- Cancels or updates bookings via database integration.
- Live Agent Support
- Connects users with customer service representatives for advanced support.

### Language Translation
- Supports multiple languages for diverse users.
- Speech-to-Text Functionality
- Enables voice input for easier interaction.

### Event Recommendations
- Displays Singapore events categorized by type, date, or location.
- Project Structure
- Backend Framework: Flask

AI Engine: Hugging Face Transformers
Database: SQLite for booking and user data
Deployment: Azure Bot Service or similar
Frontend: Optional integration with web and mobile apps

### How to Run
1. Clone the Repository

bash
Copy code
git clone https://github.com/<your-username>/singapore-tourism-chatbot.git
cd singapore-tourism-chatbot

2. Create a Virtual Environment

bash
Copy code
python -m venv chatbot_env
chatbot_env\Scripts\activate  # Windows
source chatbot_env/bin/activate  # Mac/Linux

3. Install Dependencies

bash
Copy code
pip install -r requirements.txt

4. Start the Chatbot
bash
Copy code
python app.py

5. Test the Chatbot
Send POST requests to the /chat endpoint using Postman or a Python script.

### Test Case Table
#### Feature	Description
- Greeting	Welcomes users and says goodbye.
- General Info / Visa Information	Provides Singapore-related details like culture, food, and visa requirements.
- Group Tour Itinerary Creation	Generates a full travel plan for group tours.
- Custom Tour Booking	Helps book specific tourist attractions.
- Hotel Booking	Assists users in finding and booking hotels.
- Visa Application Assistance	Collects user data to streamline the visa process.
- Flight Assistance	Redirects users to flight booking pages.
- Error Handling for Other Queries	Handles non-Singapore queries gracefully.
- Feedback Collection	Records user feedback for improvement.
- In-Person Office Info	Allows users to book on-call or in-person consultations.
- Currency Conversion	Converts and calculates currency values.
- Booking Management	Enables cancellations or modifications to bookings via a database.
- Live Agent Support	Connects users with customer service agents.
- Language Translation	Supports multiple languages for better accessibility.
- Speech-to-Text	Lets users interact with voice input.
- Event Recommendations	Displays categorized events in Singapore.

#### Future Goals
- Real-Time Booking Integration: Connect with hotel and flight APIs.
- Event Personalization: Tailor event recommendations based on user interests.
- Multichannel Support: Integrate with WhatsApp, Messenger, and Teams.
- Advanced AI Features: Use fine-tuned NLP models for greater accuracy.

#### Contact
For feedback or inquiries, contact us:

Email: singaporebot@support.com
GitHub Issues: Open an Issue

# Create a DataFrame
df = pd.DataFrame(test_cases, columns=["Feature", "Description"])

# Save to Markdown
df.to_markdown("test_cases.md", index=False)

# Save to HTML
df.to_html("test_cases.html", index=False)
Outputs:
test_cases.md: Generates a Markdown table.
test_cases.html: Creates an HTML table for web integration.

# ChatGPT-Clone

ChatGPT Clone – Flask + MongoDB

This project is a lightweight ChatGPT-style conversational web app built with Flask (Python), a simple HTML/Tailwind frontend, and MongoDB for storing chat history. It uses the OpenAI Chat Completion API to generate responses.

1) Features

Chat interface powered by OpenAI's GPT model

Message persistence using MongoDB (chat history stored per session)

Clean UI built with Tailwind CSS

Session-based conversation tracking using UUID

Flask backend with REST API

Easily extensible for authentication, multiple users, or UI enhancements

2) Tech Stack

Backend: Flask, Python, OpenAI API, PyMongo

Frontend: HTML, Tailwind CSS, JavaScript

Database: MongoDB (local or cloud via MongoDB Atlas)

3) How It Works

A user sends a message via the frontend form.

The backend appends this message to the current session history.

This history is sent to OpenAI’s API using gpt-3.5-turbo (or any chosen model).

The response from the assistant is saved in MongoDB and returned to the frontend.

Both the user and assistant messages are displayed on the screen.




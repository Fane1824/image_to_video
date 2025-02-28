# Introduction

This is a Photo-slideshow app, a web-based application that allows users to upload a sequence of images and convert them into a cohesive video. This project uses HTML, CSS, JavaScript, Python, SQL and Flask to create an intuitive and user-friendly interface for uploading, customizing, and video creation. This is an adapted version of a submission for the course project for "Introduction to Software Systems" (Spring 2024 semester). 

The project was done within a group consisting of Eshaan Sharma, Jai Aakash Gopalakrishnan, and myself. I worked on the backend and database connectivity, notably configuring the external CockroachDB database, ensuring reliable data transfer to and from the database. I also connected the different Flask routes to make the website interactive and cohesive. My last core responsibility was ensuring the images recieved from the database were stored in a format from which they could be converted into a downloadable video. In terms of the frontend, I was also responsible for designing the admin page, home page, and output page.  

# Pages

1. Landing page: The user enters the website through this page.

2. Sign in page: The user signs in through this page.

3. Sign up page: The user signs up through this page.

4. Admin page: Shows details of all users to the admins.

5. Home page: allows for the user to add images via drag-and-drop and start the process of creating a video.

6. Video creation page: Allows the user to customize the video settings, and edit the actual video.

7. Output page: When the video is finally created, this page pops up allowing the user to download.



# Share My Pics

The idea for this app came from attending various motor racing events and observing the volume of amatuer photographers with very expensive equipment
taking shots. However there are still massive number so enthusiasts who attend but do not take pictures and find on returning home
that there smart phone pictures do not cut it. Hence the idea to provide a platform for amatuer photographers to make money from good quality pictures.
Although there are plenty of sites where photos can be shared for free the concept of this site is for entusiasts who attend an events
to be able to download a high quality picture that becomes a memento of the event. Charges for images should be no more than £2 and
photographers would only be encouraged to upload their best work rather than dump hundreds of images.


## UX


A straightforward plan design was chosen with a simple blue grey colour screen. I felt it important that the design did not over power the 
photographs. Some of this design was developed on the fly and the UX will develop after inout from actual users. The most
challenging bit was the DB design. In the end a simple one table design was developed using events. However this may
need revising in future as it may not have enough flexibility.




### User Stories

- users can select from a list any event they have attended and then images will be displayed for that event

- Users can purchase images and save them to their HD

- Users can create a user account

- users can easily upload singular images for an event including price and description

- Images are protrcted by watermarks and disabling right click

- User images are low res during viewing but highres when user downloads
- 
- users can view images they have listed on the site and remove them
- 
- Users can view sales of their images





### Wire Frames

presentation2.pdf in gihub repo



## Features


### Existing Features


-Login pages requires e mail and password or users can create themselves. 

-Site is reponsive 

- User can upload images and view stock and sales. Users can select an event from a list of current database entries or add a new one in the same field

- User can view images by events. A drop down list of events in the database is provided for selection

- Users images are automatically watermarked. I have done this using Pillow after trying a JS solution. This works well 
  but results in two images. I feel there may be a better solution although this one works. In order to implement in production
  I had to save the image locally then move to S3 using Boto3

- signup. Users get sent an email confirmation when they signup.


- Django auth handles user management

- Users purchase and image and can view their downloads however once this is deleted by the owner it will be removed from the page. A potential
  archving solution may be required for a later release




### Features Left to Implement

-Develop a mechanism to work out commission on sales

-collect user bank information for transfer of income and mechanism to manage transfers

-Add pagination to the search pages

- Develop user dashboard for performance report
-
- Hide menu items that are only applicable to logged in users




## Technologies Used

- Django for main build - https://www.djangoproject.com
- Bootstrap 4 for CSS layout - https://getbootstrap.com/docs/4.0/getting-started/introduction/
- Pillow for image management - https://pillow.readthedocs.io/en/stable/
- Python for coding https://www.python.org/
- BOTO3 for uploading media to s3 - https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- jQuery for page interaction: https://jquery.com/
- AWS S3 for media and static hosting
- postgres for database- https://www.postgresql.org/
- dj-database for postgres and django link up - https://pypi.org/project/dj-database-url/
- Gunicorn for production web server - https://gunicorn.org/
- bootstrap forms to layout model forms - https://pypi.org/project/django-bootstrap-form/
- fancybox3 for lightbox - https://fancyapps.com/fancybox/3/docs/
- various django plugins including forms, Auth, Messages
- Travis for integration testing - https://travis-ci.org/
- Unittest for automated testing
- SQLlite3 for development database
- GIT for version control


## Testing

Testing strategy for each piece of developed code was to test views and urls using Unittest as the code was written in most cases
There would then be trial and error testing using developer tools and logs to solve issues. If I was unable to fix issues
I would go back a step to identify the exact bit of code that did not work then develop a solution. Finally I run through the
various User stories to check they worked

One particular difficult bug to fix was saving watermarked images when the site moved to production. When I tried to save
the watermarked pillow image to s3 with BOTO3 it did not like it. The solution in the end was to save locally then move the file using BOTO3

Another big  problem I found was the sales totals were not adding correctly. This was due to some code not working as expected and when
the code was removed all was fine.

I used Travis for integration testing and a lot of adjustments were required to I could get this working


I have not added any backway compatability for old browsers




## Deployment

Deployed to heroku. DB moved across to Postgress.  A number of values are
stored in env variables and these had to be changed for deployment. STRIPE test card numbers can be used
for dummy transactions. 


## Credits

Used for pillow resize of images -https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio



Tutorials point for general help on all subjects https://www.tutorialspoint.com/flask/flask_mail.htm
Code Institute e commerce model which helped with this build
Stack overflow for lots of general posts that put together solved many problems

Original model for footer - https://mdbootstrap.com/docs/jquery/navigation/footer/ - footer templates
text color change code on index page -https://stackoverflow.com/questions/16782498/looping-animation-of-text-color-change-using-css3
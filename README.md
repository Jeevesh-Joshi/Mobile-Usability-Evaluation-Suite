# Team 24 - Full-stack squad

# Mobile Usability Evaluation Suite 
A web-application to test the usability of mobile applications by using laboratory-based usability testing. This testing method enables the testing of mobile applications by involving real users using real devices. In it, the observer has full control over the test and can easily set the tasks – thus enabling him/her to test all usability aspects.
- Environment Setup
    ```sh
    python -m venv env
    cd env/Scripts
    ./activate
    ```
- Installing Required modules
    ```sh
   pip install -r requirements.txt
    ```
    ##### Get into the directory where ```manage.py``` is present
    
- Setting up the DB
    ```sh
   python manage.py makemigrations
   python manage.py migrate
    ```
- Starting the server
    ```sh
   python manage.py runserver
    ```
- For admin mode use
    - Username : admin
    - Password : admin

#### Working Flow
-   Firstly, we need to register the project/mobile app that needs its app to be tested. While registering, the list of the required tasks that the user/participant needs to perform will be asked.
-   After the project is registered, the user/participant will be registered. Every user will be associated with a project and will only perform the tasks that are assigned to him corresponding to that project.
-    Once the user registration is done, the observer will go to the recording section of the web app and will record videos for each of the tasks that the user performs. When the user is done will all of its tasks, the observer will move on to the testing phase where he/she will see the recording of the user corresponding to each task he/she has done. The observer will analyse the video recording and will list the problems faced by the user while operating the app.
-   Finally, the observer will mail all these details to the respective developer of the project.

#### References
-   https://stackoverflow.com/
-   https://www.djangoproject.com/
-   https://www.dynamsoft.com/codepool/web-camera-recorder-oepncv-flask.html
-   https://usabilitygeek.com/usability-testing-mobile-applications/


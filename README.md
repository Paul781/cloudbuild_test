### File Structure

```yaml
cloudbuild_test
├── app
│   └── app.py
├── test
│   └── test_app.py
├── cloudbuild.yaml
├── Dockerfile
├── README.md
├── requirements.txt
```
- The code for application is under the app folder named app.py
- The code for test is under the test folder named test_app.py

Flask is used to implement the API backend. Unit test is done by pytest. CloudBuild is the CI tool.



### Deployment Step

1. run the unit test locally
2. if passing all the unit tests, push code change to the develop branch of the github repo (version number can be changed in cloudbuild.yaml file)
3. cloud build will be triggered and go to the gcp console to check the cloudbuild job status
4. after the cloudbuild job finishes, go the gcr.io to check the `flask-api` image and tag
5. create pull request from develop branch to master branch
6. merge the pull request to master branch



### Build and Run Locally
Standalone API server run with:

```shell
cd cloudbuild_test
docker build --build-arg var_version=2.0 --build-arg var_commitsha=aaaccc -t flask-app:latest .
docker run  -p 80:80 flask-app
```
Go to browser and visit the `http://0.0.0.0/version`  
`var_commitsha` and `var_version` are the commit sha and version number

### Unit Test
Standalone unit tests run with:

```shell
pip install pytest
cd cloudbuild_test
pytest -v
```
After testing, submit a pull request to merge changes with **master**.

### Risk
1. we can send any http request to the application which is not secure.
JWT or https is required for the application
2. The github repo is public so anyone can read the code to understand the CI process.
3. The vulnerability scan should be enabled for docker image
4. The git hook should be enable to check the commit. for example, if you do not have the permission, you can not commit the code
5. Enable the webhook in github repo so that the unit test can be run before the pull request is merged

### CloudBuild
- There is one cloud build trigger in my onedirect project of GCP.
- Any push to the develop branch of this repo will trigger the cloud build to build the docker image using the cloudbuild.yaml file.
- The docker image will be stored in the gcr.io in my ondirect project

### Version Control
Change the version nummber in the cloudbuild.yaml file.
```markdown
substitutions:
  _VERSION: "2.0"
```
Cloudbuild will use this version number as the tag for docker image
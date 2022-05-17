# QAproject2
## Author - Kieran Armstrong

## Objective 
To create a simple application which consists of four services that work together in order to achieve functionality. 
Service one will be used to render templates and communicate with the other three services. 
Services two and three will both generate a random object, which will both be used to create an object in service four.

The application will generate different types of weapons in a fantasy-style setting. Service two will generate a weapon type and service three will generate a damage multiplier for the weapon. Service four will then use these to generate the final weapon. Service one will then deliver this information to the user.

The scope of the project includes the following:

-An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
-An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
-If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
-The project must follow the Service-oriented architecture that has been asked for.
-The project must be deployed using containerisation and an orchestration tool.
-As part of the project, you need to create an Ansible Playbook that will provision the environment that your application needs to run.
-The project must make use of a reverse proxy to make your application accessible to the user.

The technologies that are to be used include:

-Kanban Board: Asana or an equivalent Kanban Board
-Version Control: Git
-CI Server: Jenkins
-Configuration Management: Ansible
-Cloud server: GCP virtual machines
-Containerisation: Docker
-Orchestration Tool: Docker Swarm
-Reverse Proxy: NGINX

## Project Management
### Trello
I have decided to use Trello for the purpose of project management. I decided to use Trello as it provides a visual and user-friendly interface for keeping track of tasks, allowing me to manage my time efficiently. It also has features that allow for storing documentation in a centralised location, making it easier to organise the necessary documentation.
![trello](https://github.com/Kieran-Armstrong/QAproject2/blob/main/images/trello.PNG)

### Entity Diagram
I made a simple entity diagram to help with planning the object to be generated for the user
![ed](https://github.com/Kieran-Armstrong/QAproject2/blob/main/images/ed.PNG)

### Risk Assessment 

The risk assessment for this project included both general risks that will apply to most projects as well as more specific risks that were realised throughout the development process.
![ra](https://github.com/Kieran-Armstrong/QAproject2/blob/main/images/ra.PNG)

## Pipeline 

As a continuous development pipeline, a number of factors are required for the project to run as it should. Any time the code is updated, unit testing must be carried out in order to maintain functionality.
The webhook automates the running of the pipeline in Jenkins any time new code is pushed up to the main branch in the GitHub repo.
Ansible is then used to install any and all dependencies, implement the swarm and restart NGINX if and when necessary.
Jenkins will then facilitate the use of the code in the GitHub repo and deploy the stack using docker-swarm.
The following diagram is a very simplified version of this pipeline:
![pipeline](https://github.com/Kieran-Armstrong/QAproject2/blob/main/images/pipeline%20diagram.PNG)

## Services 

Below is a simple diagram showing how the services should interact with one another 
![services](https://github.com/Kieran-Armstrong/QAproject2/blob/main/images/services.PNG)

## Testing 

Unit testing was utilised for this project using pytest. 

## Issues during development

I encountered numerous set backs due to an issue with GCP. I have experienced issues with my billing account throughout the duration of the project.
I am in contact with GCP support to hopefully have this resolved and resume the functionailty of the application

## Future Developments
- In order to make for easier development, I should have made use of multiple branches on GitHub. 
- would like to develop the application further and implement a wider range of uses for the end user
- Explore ways in which downtime can be reduced during updates, with the target of eliminating downtime where possible

## Acknowledgements

Victoria Sacre - QA tutor
Earl Gray - QA tutor
Peers in 22MAREnable1 cohort 

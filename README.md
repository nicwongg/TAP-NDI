# TAP-NDI Assignment

## Problem Statement
In the recent years, there have been a lot of scam calls that have been happening.
These calls would often contain a +65 prefix, and would attempt to ask for the victims' personal information, such as their names, NRIC numbers and bank account details. It is worth noting that some +65 calls are legitimate calls. 
These scam calls create a lot of noise that could hinder public officers from contacting citizens for legitimate reasons.

Although there are some measures such as ScamShield which tries to passively block scam messages and calls, it is still not a foolproof solution. Some calls still do get through. 

## Proposed Solution
To have a proactive solution that allow citizens to verify if the caller is indeed from a legitimate source.

- Citizens can verify if the caller is a public officer from a governmental ministry.
- Public officers can prove their identity when they are trying to perform their duties.

### Used service
- Singpass login

### Architecture
The application is containerized and hosted on AWS Fargate. There is a CI/CD pipeline that runs tests, containerizes, and deploys the new versions into AWS ECR and Fargate.

![Architecture Diagram](https://i.ibb.co/KWRJgzC/TAP-NDI.png)

### Wireframing
![Wireframe](https://gcdnb.pbrd.co/images/PYCPd1W254HH.png?o=1)

### Future implementation
In the current implementation, the solution is only for governmental ministries. In future implementations, this could be extended to private organisations such as banks and even e-commerce platforms, where a huge portion of scam calls are prevalent.

It would be best to have this as an additional feature (callee only) in our Singpass application as most people should already have the Singpass application in their phone.

## Set up information
Callee portal: localhost:5000

Caller portal: localhost:5000/caller

The callee side will always use `S****252G` when logging in - this is to mock the id that's provided/used by Singpass.
So the caller should use `S****252G` when prompted for the NRIC to key in.

Available caller emails for use `bob@moh.gov.sg`, `jerry@mom.gov.sg`, `james@moh.gov.sg`, `tom@moe.gov.sg`.

### Running it locally
To run it locally, you can run the `flask run` command in the main directory.

### Hosting
The application is also hosted on Amazon ECS: `54.251.11.192:5000`
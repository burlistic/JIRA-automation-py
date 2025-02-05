# JIRA Automation Script

Set up automation script to match requirements for automating the stopping, creating and starting a new JIRA sprints for a scaled scenario where multiple teams want to use the same project on a set cadence. Used to be supported by the on prem addition.

Using the JIRA api to achieve the same results. Decided to also use TDD and learn more about dependancies injection in Python, so potentially a little over engineered. Could be a script with testing done against a dummy JIRA sandbox.

### Gets all sprint for a give Project / board ✅

### Validates there is one active sprints and two future sprints ✅

### Create a new future sprint

### Transfer issues from open sprint to the next

### Close the old sprint

### Starts the new sprint

## Set up

### Add to AWS as a Lamda

### Add secrets / create JIRA API token not linked to my person account

### Test against dummy sandbox and then make live

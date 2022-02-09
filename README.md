# Process-Mining-CNJ
##
## Web application that, from a .csv file sent, processes and generate an svg image with the Directly Follows Graph (DFG), from EventsLogs

#
![demostration](demostration.gif)

#
## How I test:
1. Follow the steps below to make the __Client__ active.
1. Follow the steps below to make the __Server__ active.
1. Do both running at the same time.
1. Enter the route [http://localhost:4200/](http://localhost:4200/) in your browser.
1. Drop one __.csv__ file, following this pattern:
    | Case | ActivityCode | Start | End |
    | :--- | :--- | :--- | :--- |
    | 657797 | A1 | 2016/06/01 07:25:09.000 | 2016/06/01 07:53:49.000 |
    | 657797 | A2 | 2016/06/01 07:53:50.000 | 2016/06/01 07:55:29.000 |
    | 657797 | A3 | 2016/06/01 07:55:30.000 | 2016/11/01 10:55:50.000 |
    | ... | ... | ... | ... |
1. Ps: .csv _sep_ will be __";"__.
1. Click on _"Send File"_.
1. Wait for the backend to generate the EventLog.
1. Wait for the backend to generate the DFG.
1. Analyze the DFG that will appear on the same page.

### Attencion, You need install GraphViz
```sh
sudo apt-get install graphviz  # for unix-based os
```
for Windows or OSX, see [https://graphviz.org/](https://graphviz.org/)

#
## For Boot Client:
```sh
cd client
#  Use the NVM - Node Version Manager - to choice the version 14.19.0
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
nvm install 14.19.0
nvm use 14.19.0
#  Install the angular-cli and others dependences
npm install -g @angular/cli
npm install
#  Run the client
ng serve -o
```

## For Boot Server:
```sh
# Enter in your virtural env
cd server
pip install -r requirements.txt
flask run
```
#
## Objectives

### Front-End

- [x] pages/components Angular
- [x] Integration with the backend
- [x] Forms to send csv to backend
- [x] Component to visualize svg image

### Back-End

- [x] Routes Flasks
- [x] Get csv image from frontend
- [x] Transforms csv to Eventlog
- [x] Aply process discover DFG in Eventlog
- [x] Create SVG from DFG results in text

### Extra

- [x] Architecture Blueprints to Flask 
- [x] Architecture Scalable to Angular 
- [ ] Have a tab with general information about the data
- [ ] Implement filtering functions on the data

#
## Author
| <a href="https://github.com/ericxlima"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/58092119?v=4" width="100px;" alt="Eric"/></a> |
| :----: |
| [Eric de Lima](https://github.com/ericxlima) |
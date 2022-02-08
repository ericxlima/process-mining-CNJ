Attencion, You need install GraphViz
```sh
sudo apt-get install graphviz
```

## For Client:
```sh
cd client
nvm install 14.19.0
nvm use 14.19.0
npm install -g @angular/cli

ng serve
```


## For Server:
```sh
# Enter in your virtural env
cd server
pip install -r requirements.txt
flask run
```


## Front-End

- [x] pages/components Angular
- [ ] Integration with the backend
- [x] Forms to send csv to backend
- [ ] Component to visualize svg image

## Back-End

- [x] Routes Flasks
- [x] Get csv image from frontend
- [x] Transforms csv to Eventlog
- [x] Aply process discover DFG in Eventlog
- [x] Create SVG from DFG results in text

## Extra

- [x] Architecture Blueprints to Flask 
- [ ] Architecture Scalable to Angular 
- [ ] Have a tab with general information about the data
- [ ] Implement filtering functions on the data

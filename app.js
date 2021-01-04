//express - routing, scalability
let {PythonShell} = require('python-shell')
const express = require("express") // import module
const path = require("path");
const fs = require("fs");
const app = express(); //make app
const port = 3000;
const directory = 'output';
 

// EXPRESS SPECIFIC STUFF
app.use('/static', express.static('static'))
app.use('/output', express.static('output'))
app.use(express.urlencoded())

// PUG SPECIFIC STUFF
// Set template engine as pug
app.set('view engine', 'pug')
// Set view directory
app.set('views', path.join(__dirname, 'views'))

// END POINTS
// Pug demo end point

app.get('/', function(req, res){
    res.status(200).render('index.pug');
    fs.readdir(directory, (err, files) => {
        if (err) throw err;
      
        for (const file of files) {
          fs.unlink(path.join(directory, file), err => {
            if (err) throw err;
          });
        }
    });
});

app.post('/', (req,res)=>{
    text = req.body.text
    let outputToWrite = `${text}`
    fs.writeFileSync('output/example.txt', outputToWrite);
    PythonShell.run('texttohand.py', null, function (err) {
        if (err) throw err;
        console.log('finished');
    });
    res.status(200).render('download.pug');
});

app.listen(port, ()=>{
    console.log(`This app started successfully on port ${port}`);
});


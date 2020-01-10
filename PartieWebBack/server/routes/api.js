const express = require('express');
const MongoClient = require('mongodb').MongoClient
const bodyParser= require('body-parser')
var ObjectID = require('mongodb').ObjectID;
const router = express.Router();
const cors = require('cors');
const multer = require('multer');
const app = express();
const spawn = require('child_process').spawn;
const exec = require('child_process').exec;

MongoClient.connect('mongodb://localhost:27017/test', (err, db) => {
  if (err) return console.log(err)

  
  let dbase = db.db("test");
// File upload settings
const PATH = '../uploads';
let storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, PATH);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname + Date.now()+ '.csv')
 }
});

let upload = multer({
  storage: storage
});


// File upload 1 fluxtest settings
const PATH2 = '../InputFiles';
let storage1 = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, PATH2);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname + Date.now()+ '.csv')
 }
});

let upload1 = multer({
  storage: storage1
});


// File upload 2 fluxtest settings
const PATH3 = '../InputFiles2';
let storage2 = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, PATH3);
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname + Date.now()+ '.csv')
 }
});

let upload2 = multer({
  storage: storage2
});



app.use(upload.array());
app.use(cors());

const sendError = (err, res) => {
    response.status = 501;
    response.message = typeof err == 'object' ? err.message : err;
    res.status(501).json(response);
};

router.post('/upload', upload.single("file"), function (req, res) {
  if (!req.file) {
    console.log("No file is available!");
    return res.send({
      success: false
    });

  } else {
    console.log('File is available!');
    return res.send({
      success: true
    })
  }
});

router.post('/uploadhost', upload1.single("file"), function (req, res) {
  if (!req.file) {
    console.log("No file is available!");
    return res.send({
      success: false
    });

  } else {
    console.log('File is available!');
    return res.send({
      success: true
    })
  }
});

router.post('/uploadsourceDP', upload2.single("file"), function (req, res) {
  if (!req.file) {
    console.log("No file is available!");
    return res.send({
      success: false
    });

  } else {
    console.log('File is available!');
    return res.send({
      success: true
    })
  }
});



router.get('/users', (req, res) => {
    dbase.collection('mycollection').find().toArray( (err, results) => {
      res.send(results)
    });
  });

router.get('/flux', (req, res) => {
    dbase.collection('currency').find().toArray( (err, results) => {
      res.send(results)
    });
  });



router.get('/shellRequest', function(req, res) {
  const command = spawn('/home/ansibleM/tacheOne/submit.sh', [ req.query.patern || '']);
  const output  = [];
  command.stdout.on('data', function(chunk) {
    //output.push(chunk);
    console.log(chunk.toString());
  }); 

  command.on('close', function(code) {
    if (code === 0)
      res.send(Buffer.concat(output));
    else
      sendError; // when the script fails, generate a Server Error HTTP response
  });
});

router.get('/fluxRequest', function(req, res) {
  const command = exec('/home/ansibleM/tachetelnet/AnsibleProject/FirstShell.sh');
   const output  = [];
  command.stdout.on('data', function(chunk) {
    //output.push(chunk);
    console.log(chunk.toString());
  });

  command.on('close', function(code) {
    if (code === 0)
      res.send(Buffer.concat(output));
    else
      sendError; // when the script fails, generate a Server Error HTTP response
  });

});

  
});
module.exports = router;



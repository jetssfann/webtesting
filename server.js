const express = require ('express');
const mongoose = require ('mongoose');
const bodyParser = require ('body-parser');


const app = express();

//BODY-PARSER Middleware

app.use(bodyParser.json());

// DB Config

const db = require('./config/keys').mongoURI;

// Connect to Mongo
mongoose.connect(db)
  .then(() => console.log('MongoDB Conected...'))
  .catch(err => console.log(err));



const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`server started on port ${port}`));

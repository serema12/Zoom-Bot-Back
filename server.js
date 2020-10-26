const express = require("express")
const dotenv = require("dotenv")
const cors=require("cors")
const chalk = require("chalk")

//routers
const zoomRouter = require('./router/zoomRouter')
// set environment
dotenv.config()

// server start
const app = express()
const PORT = process.env.PORT || 4000
// to avoid different polocies between server and frontend
app.use(cors())

app.use((req,res,next)=>{
    res.header('Access-Control-Allow Origin','*')
    next();
})

app.use('/',zoomRouter);

app.listen(PORT,()=>{
    console.log(chalk.yellow("Server started at PORT") + chalk.green(PORT))
})



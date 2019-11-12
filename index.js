// libs
const express = require("express")
const expressLayouts = require("express-ejs-layouts")
const bodyparser = require("body-parser")
const { execSync } = require("child_process")
const path = require("path")

// preparing to create server
const app = express()
const port = process.env.PORT || 3333
app.use(bodyparser.json())
app.set("view engine", "ejs")
app.use(expressLayouts)

// training airline analysis
function train() {
  try {
    console.log("Training Analyzer");
    execSync(`python3 ${path.resolve("./src/airline-training.py")}`)
    console.log("Successfully trained")
  } catch (error) {
    train()
  }
}
train()

// creating server
app.listen(port, () => {
  console.log(`Server running on port ${port}`)
  console.log(`Access: http://localhost:${port}/`)
})

// routes
// home
app.get("/", (req, res) => {
  res.render("pages/home", {
    output: "",
    input: ""
  })
})

// free text
app.get("/freeText", (req, res) => {
  res.render("pages/freeText", {
    output: "",
    input: ""
  })
})

// free text result
app.get("/freeText/:input", (req, res) => {
  let input = JSON.stringify(req.params.input.replace(/%0D%0A/g,"\n")).replace(/\"/g,"")
  
  exec(`echo "${input}" | ${path.resolve("./src/simple-analysis.py")}`, (error, stdout) => {
    let output
    error ? output = error : output = stdout
    res.render("pages/freeText", {
      output,
      input
    })
  })
})

// airline analysis
app.get("/airlineAnalysis", (req, res) => {
  res.render("pages/airlineAnalysis", {
    output: "",
    input: ""
  })
})

// airline analysis result
app.get("/airlineAnalysis/:input", (req, res) => {
  let input = JSON.stringify(req.params.input.replace(/%0D%0A/g,"\n")).replace(/\"/g,"")
  
  exec(`echo "${input}" | python3 ${path.resolve("./src/airline-analysis.py")}`, (error, stdout) => {
    let output
    error ? output = error : output = stdout
    res.render("pages/airlineAnalysis", {
      output,
      input
    })
  })
})
const { exec } = require("child_process")

exec("./main.py", (error, stdout) => {
  if (error) {
    console.log("erro")
  } else {
    console.log(stdout)
  }
})
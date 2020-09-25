const express = require('express')
const { homedir } = require('os')


const app = express()
const PORT = 7000


app.route('/home').get((req, res) =>{

})

app.listen(PORT, ()=> {
    console.log(`Running application on port ${PORT}`)
})


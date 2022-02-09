const dgram = require('dgram');
const client = dgram.createSocket('udp4');

const address = '0.0.0.0'
const port = '3000'

client.send('Yo ssup', port, address, (err)=>{
    if(err) console.log(err)

    console.log("sent");
    client.close();
})


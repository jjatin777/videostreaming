const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const address = '0.0.0.0'
const port = '8000'

server.on('error', (err) => {
  console.log(err);
  server.close();
});

server.on('message', (msg, rinfo) => {
  console.log(`server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
});

server.on('listening', () => {
  console.log(`server listening ${address}:${port}`);
});

server.bind({
    address,
    port,
    exclusive: true
  });


  // //////////////////

const client = dgram.createSocket('udp4');

// const address = '0.0.0.0'
// const port = '3000'

client.send('Yo ssup dawg at 3000 i am from 8000', '3000', address, (err)=>{
    if(err) console.log(err)

    console.log("sent");
    client.close();
})
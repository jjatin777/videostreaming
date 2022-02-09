const dgram = require('dgram');
const server = dgram.createSocket('udp4');

const address = '0.0.0.0'
const port = '3000'

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



const client = dgram.createSocket('udp4');

// const address = '0.0.0.0'
// const port = '8000'

client.send('Yo ssup dawg at 8000 i am from 3000', '8000', address, (err)=>{
    if(err) console.log(err)

    console.log("sent");
    client.close();
})
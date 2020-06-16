/*
  This is an express version of a possible prometheus server
  WIP 
*/

var amqp = require('amqplib/callback_api');
var express = require('express');

var counter = 0;

amqp.connect('amqp://localhost', function(error0, connection) {
    if (error0) {
        throw error0;
    }
    connection.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }
        var queue = 'hello';

        channel.assertQueue(queue, {
            durable: false
        });

        console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", queue);

        channel.consume(queue, function(msg) {
            counter++;
            console.log(" [x] Received %s", msg.content.toString());
        }, {
            noAck: true
        });
    });
});

const app = express()
const port = 3000

app.get('/', function (req, res) {
    console.log("Message Number " + counter);
    res.send('Hello World!');
})

app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`));


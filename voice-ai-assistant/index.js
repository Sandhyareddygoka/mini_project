const express = require('express');
const bodyParser = require('body-parser');
const VoiceResponse = require('twilio').twiml.VoiceResponse;
const axios = require('axios');

const app = express();
app.use(bodyParser.urlencoded({ extended: false }));

app.post('/voice', async (req, res) => {
  const userInput = req.body.SpeechResult || 'Hello';

  let aiReply = 'Sorry, I could not understand.';
  try {
    const vapiRes = await axios.post(
      'https://api.vapi.ai/assistant-response',
      { message: userInput },
      { headers: { Authorization: 'Bearer YOUR_VAPI_API_KEY' } }
    );
    aiReply = vapiRes.data.response;
  } catch (err) {
    console.error(err.message);
  }

  const twiml = new VoiceResponse();
  twiml.say({ voice: 'Polly.Raveena', language: 'en-IN' }, aiReply);

  res.type('text/xml');
  res.send(twiml.toString());
});

app.listen(5000, () => {
  console.log('Server running on port 5000');
});
const mongoose = require('mongoose');

const mongoURI = 'mongodb+srv://PPE:Ritu0101@cluster0.enpkimw.mongodb.net/ppedetect?retryWrites=true&w=majority&appName=Cluster0';

const mongoDB = async () => {
  console.log("Attempting to connect to MongoDB..."); // 🔍 Debug log
  try {
    await mongoose.connect(mongoURI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log("✅ Connected to MongoDB");
    const fetched_data = await mongoose.connection.db.collection("PPE");
    fetched_data.find({}).toArray(function(err, data){
        if(err) {
            console.log(err);
        }else {
            console.log();
        }
    } )
  } catch (err) {
    console.error("❌ Error connecting to MongoDB:", err);
  }
};

module.exports = mongoDB;

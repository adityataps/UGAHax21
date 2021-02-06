import firebase from "firebase/app"
import "firebase/auth"
import "firebase/firestore"

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyBI2Mk4pMvYMkZ8ATKDu3a_7mS9a6r-dng",
    authDomain: "ugahack21.firebaseapp.com",
    projectId: "ugahack21",
    storageBucket: "ugahack21.appspot.com",
    messagingSenderId: "468792756154",
    appId: "1:468792756154:web:76c6cc1282089d4cddbf83",
    measurementId: "G-Z227MJG88R"
};

firebase.initializeApp(firebaseConfig)
export const auth = firebase.auth()
export const firestore = firebase.firestore()
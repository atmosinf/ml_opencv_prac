## Screenshots from the lectures<br>
### face_detect.py
![1](screenshots/1.png)<br><br>
![2](screenshots/2.png)<br><br>
![3](screenshots/3.png)<br><br>
![4](screenshots/4.png)<br><br>
![5](screenshots/5.png)<br><br>
**haar cascades are really sensitive to noise**<br><br>
![6](screenshots/6.png)<br><br>
![7](screenshots/7.png)<br><br>
![8](screenshots/8.png)<br><br>
![9](screenshots/9.png)<br><br>
![10](screenshots/10.png)<br><br>
![11](screenshots/11.png)<br><br>
![12](screenshots/12.png)<br><br>
**but by when you tweak it to detect more faces, it is also more susceptible to noice. so even though haarcascades are popular and easy to use, they're not what you'd use in most real computer vision prokjects**<br><br>
### faces_train.py
![13](screenshots/13.png)<br><br>
![14](screenshots/14.png)<br><br>
![15](screenshots/15.png)<br><br>
**the face recognizer is essentially trained now. but if you want to use this face recognizer in another file, we'll have to manually repeat this process of adding those images to a list and getting the corresponding labels, converting that to numpy arrays, etc. opencv allows us to save this trained model, so that we can use it elsewhere, just by using the yaml source file**<br><br>
![16](screenshots/16.png)<br><br>
### face_recognition.py
![17](screenshots/17.png)<br><br>
![18](screenshots/18.png)<br><br>
![19](screenshots/19.png)<br><br>
![20](screenshots/20.png)<br><br>
![21](screenshots/21.png)<br><br>
![22](screenshots/22.png)<br><br>
**we can see that opencv's built in face recognizer is not the best. and we only trained it on a total of 100 images.a deep learning model can perform much better at image recognition**<br><br>
### Capstone (train your own ML model)
![23](screenshots/23.png)<br><br>
![24](screenshots/24.png)<br><br>
**the above 2 packages were created by the author of the video. no need to install canaro if you don't have a GPU. canaro also installs tensorflow by default**<br><br>
**get the [simpsons characters dataset](https://www.kaggle.com/alexattia/the-simpsons-characters-dataset) from Kaggle**<br><br>
**Go to kaggle.com/notebooks**<br><br>
![25](screenshots/25.png)<br><br>
![26](screenshots/26.png)<br><br>
![27](screenshots/27.png)<br><br>
**we also installed caer and canaro in our local machine so that we can experiment and work with it if needed**<br><br>
![28](screenshots/28.png)<br><br>
![29](screenshots/29.png)<br><br>

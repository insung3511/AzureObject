## AzureObject
프로젝트 저장소 업로드 
2018 June 16 

## Project New Begin
~~프로젝트가 취소가 아닌 진행으로 되었다..ㅋㅋㅋㅋㅋㅋㅋㅋㅋ </br>
솔직히 말해서 취소했다는것은 그냥 혼자서 적은 것이지, 딱히 취소를 한다. 라고 해서 큰 의미는 없었다. </br>
프로젝트에 대한 상세한 설명은 아래에 적어놓았다. ~~

## A2ZObject Project
" A2ZObject " 프로젝트는 Microsoft의 Azrue 서비스에 Custom API를 활용한 프로젝트이다. 사실 이 프로젝트를 openCV로 진행을 할려고 했으나 여러가지 변경 사항을 사람이 노가다를 해가면서 ㅈㄴ 힘들어 죽는 일을 할 필요가 없다고 판단이 되어서 머신 러닝으로 진행하게 되었다. </br>
이 프로젝트는 사실 하드웨어 소프트웨어 융합하여 하는 프로젝트이다. 하드웨어에는 라즈베리파이, EV3가 도입이 될 예정이고 소프트웨어는 Python와 Microsoft의 Azrue를 사용할 예정이다. </br>
</br>
<h4> 그래서 뭐하는 프로젝트 인데요 </h4>
좋은 질문 입니다. ~~자문자답ㅎ~~ </br>
쉽게 설명하면 부품을 분류하는 로봇을 만드는 프로젝트 입니다. 다만 그 부품들이 레고의 빔이라는 부품이라는 것이 다른것이죠. 저희가 직접 부품을 분류하는 로봇을 만들기에는 너무나도 거창하고 비용 그리고 실력이 없기 때문에 저희는 레고의 부품 중인 <a href=""> "빔" </a>을  부품을 대처 하여 활용할것이다. </br>

## Software Guide
<b> <u> SoftWare Guide </u> 부분은 <a href="https://docs.microsoft.com/ko-kr/azure/cognitive-services/custom-vision-service/python-tutorial"> Microsoft 공식 문서 </a> 를 참고하여 작성이 되었습니다. 이 글의 오류가 있을수 있으니 원본 문서를 먼저 읽어 보시는것을 추천드립니다 </b> </br>
일단 첫번째로 공부에 필요한 사진을 찍어 줘야한다. 공부할 사진을 Google와 Bing에서 20분 동안 뒤지닌까 80장 정도 나온다. </br>
그래서 내가 직접 데이터를 만들기로 했다. ~~사진을 데이터라고 하닌까 멋져보임ㅋ~~~ </br>
사진을 찍기 위해서 웹캠이 필요한데, 나는 지금 웹캠이 없다. 그래서 노트북에 있는 카메라를 이용하기로 했다. </br>
그리고 부품을 여러방면에서 찍어야 하기 때문에 부품을 돌려줄 장치도 필요하다. 일단 결론 부터 말하자면 아래 사진으로 설명을 하진 않겠다. 
![TestPic.png](https://github.com/insung3511/AzureObject/blob/master/bottom/opencv77.png)
이렇게 했는데 한 부품당 눕혀서 1000장 세워서 1000장 해서 한 찍는데만 5분 가량 소요 된거 같다. </br>
찍을때 사용한 코드는 Camera-Python 디렉토리에 가면 있다. (2018년 7월 28일 기준 업로드 안함) </br>
그 코드는 사실 StackOverFlow에서 누군가 올려놓은 코드 인데, 출처를 못 남겨 놓았다... 나중에 방문기록 찾으면 올릴게요... </br>
데이터를 만드는데 화질이 생각외로 높다 보니 720HD로 되어 있어서 꽤 용량이 크다. 1000장에 2.41GB가 나왔다. </br>
</br>
사진들을 모두 찍고 <a href="https://customvision.ai"> Custom Vision Portal </a>에 들어가서 사진 업로드와 공부를 시켜줘야 한다. </br>
사진들을 모두 업로드를 하고 공부를 시킨후에서 코드로 작성을 해서 인공지능을 테스트한 값에대한 결과물을 텍스트로 받고 싶었는데, 코드를 아무리 찾아봐도, 결과만 받을수 있는 코드가 없다. ~~구글쓰세요...구글이 짱이에요~~ </br>
결국 <a href="https://docs.microsoft.com/ko-kr/azure/cognitive-services/custom-vision-service/python-tutorial"> Python 자습서 </a>를 보고 코드로 프로젝트를 생성하고, 파일을 업로드하고 결과를 얻는 방식으로 하기로 했다. </br>
코드가 좀 길고, 디렉토리가 이러저러 많아서 그런지 좀 많이 헷갈린다. </br>
Bottom 디렉토리와, Top 디렉토리가 비슷비슷하고 컴퓨터마다 차이가 있겠지만 사진을 업로드를 하는데에 대한 시간을 생각하면 1000장이라는 사진은 꽤 오래 걸린다. </br>
사진을 101장으로 줄이고 다시 업로드를 하고 공부를 시키는대 까지 최소한 20~30분 이상은 걸린다. </br> 

<pre>
A2ZObject 공부중....
</pre>

## Contact me
----------------------------------------
If you have problem about this code, then contect me. </br>
Email : insung.park123@gmail.com </br>
Facebook : https://www.facebook.com/insung.bahk </br>
</br>
If you want to give me some money... Please money send here! </br>
Bitcoin : 17qKUu57aUBcvx9T1ea8Ga87EPnDdmwAEP </br>
Ether : 0xdFE8D1536deE8F839Ede7c1f3A0c44116287D931  
Bitcoin Cash : qp90gf09r3y3h06czmtnsfhz9w7s90se4s72vd9pam </br> 
</br>
🙇‍♀️👾🤩Thank you! 🤩👾🙇‍♂️ 
----------------------------------------

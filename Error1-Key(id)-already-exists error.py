duplicate key value violates unique constraint "store_collection_pkey"
DETAIL:  Key (id)=(2) already exists.




WHEN YOU GET AN ERRO LIKE THE ONE ABOVE, IT MEANS THAT YOU ARE TRYNG TO CREATE A NEW OBJECT, BUT THE ID OF THAT TABLE DOES NOT AUTO INCREMENT.
TO FIX THIS, YOU NEED TO RUN THIS CODE THAT TELS THAT TABLE TO AUTOINCREMENT



SELECT setval('tablename_id_seq', (SELECT MAX(id) FROM tablename)+1);



In postgres, run this command in the pgadmin




More error questions - seek help from this website.    //https://forum.codewithmosh.com/t/django-saving-objects/12511

































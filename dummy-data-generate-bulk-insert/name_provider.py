from faker.providers import BaseProvider

class SurnameProvider(BaseProvider):
    def surname(self):
        surnames = [
    "Okeke", "Okonkwo", "Nwosu", "Eze", "Obi", "Onwuchekwa", "Nwankwo", "Okechukwu", "Chukwu", "Okoro", "Uche", "Nwafor", "Ezebuiro", "Anyanwu", "Mbanefo", "Maduka", "Ike", "Nnaji", "Obinna", "Ifeanyi", "Onoh", "Nweke", "Chibueze", "Ekechukwu", "Duru", "Nwankpa", "Ozonwafor", 
    "Okezie", "Udochukwu", "Nnamdi", "Osuji", "Orji", "Madu", "Njoku", "Ogwuegbu", "Oguejiofor", "Agu", "Ubah", "Ojukwu", "Nwachukwu", "Amaechi", "Iheanacho", "Ogbodo", "Chukwuma", "Ikpeazu", "Nwoko", "Ejiofor", "Igwe", "Ezem", "Akubueze",
    "Osuagwu", "Ezebuiro", "Nwandu", "Ezenwa", "Obiano", "Nwaokorie", "Odogwu", "Okwudili", "Amadi", "Akunna", "Chukwudum", "Mbah", "Ogbonna", "Onyema", "Onwudiwe", "Onuigbo", "Omego", "Nwosu", "Nwanze", "Ozigbo",
    "Chijindu", "Ebubedike", "Enyinnaya", "Ibeneme", "Iloegbunam", "Iroha", "Isiadinso", "Izuakor", "Izuchukwu", "Jideofor", "Kenechukwu", "Kalu", "Korie", "Madueke", "Mba", "Mgbeke", "Mgbemena", "Muo", "Muojekwu",
    "Nduka", "Ndulue", "Ngwoke", "Nkwocha", "Nwadike", "Nwaneri", "Nwankwoala", "Nwanze", "Nwaokobia", "Nwaora", "Nwasike", "Nweze", "Nwobodo", "Nwokedi", "Nwokoma", "Nwokocha", "Nworie", "Nwosu", "Nwude", "Nwufo",
    "Obiefuna", "Obijiaku", "Obinwa", "Obioha", "Obodoechina", "Obodo", "Obodoako", "Obodoekwe", "Obunadike", "Ochudo", "Odoemelam", "Odunukwe", "Ofodile", "Ofoegbu", "Ofor", "Ogbuagu", "Ogbuji", "Ogugua", "Ohazulike", "Okafor", "Okeke", "Okoli", "Okonkwo", "Okorie", "Okpara", "Okpala", "Okwuosa", "Okwudili", "Okwueze", "Olisa",
    "Omeje", "Omenife", "Onah", "Onuchukwu", "Onuh", "Onwubiko", "Onwugbufor", "Onwukwe", "Onwuliri", "Onyenemezu", "Onyenucheya", "Onyilimba", "Onyimba", "Onyishi", "Onyemobi", "Onyemelukwe", "Onyenze", "Onwuamaeze", "Onwuasoanya", "Onwuchuruba",
    "Onwufuju", "Onwukeme", "Onwuliri", "Onwuma", "Onwumere", "Onwurah", "Onwuzulike", "Oparaku", "Opara", "Oranika", "Orjiakor", "Orjioke", "Orjiugo", "Orlu", "Orutugu", "Oseji", "Osinachi", "Osuagwu", "Oti", "Otiji",
    "Otolokpo", "Otuokere", "Otuonye", "Oweredimma", "Oyeoku", "Ozoemena", "Ozoemelam", "Ozonma", "Ozor", "Ozuruigbo", "Ubah", "Ubani", "Udechukwu", "Udeh", "Udemba", "Udenkwo", "Udensi", "Udo", "Udobi", "Udokamma",
    "Udogu", "Udoh", "Ukaegbu", "Ukpabi", "Ukpata", "Umeh", "Umunna", "Unachukwu", "Unigwe", "Uwakwe", "Uzochukwu", "Uzor", "Uzuegbu", "Abanobi", "Abazie", "Achonu", "Adimora", "Adindu", "Aduaka", "Agomuo", "Aguta", "Ahamefule", "Ajunwa", "Akachukwu", "Akam", "Akanazu", "Akwue", "Amadikwa", 
    "Amatokwu", "Amobi", "Anachebe", "Anazodo", "Anene", "Anidiobi", "Anikamadu", "Anosike", "Anumudu", "Anyaehie", "Anyanele", "Anyiam", "Anyichie", "Arochukwu", "Asiegbu", "Atuegwu", "Azubuike", "Azuka", "Buchi", "Chibogu", "Chibundu", "Chidimma",
    "Chiedozie", "Chijoke", "Chikezie", "Chinemelum", "Chinonyelum", "Chinwendu", "Chizoba", "Chukwuanu", "Chukwuka", "Chukwuneke", "Dimgba", "Dike", "Echefu", "Echezona", "Edeani", "Edeh", "Edochie", "Efobi", "Ejimofor", "Ekene",
    "Ekwueme", "Eluemuno", "Emenike", "Emesaraonye", "Enemuo", "Enweonwu", "Erebor", "Eriobuna", "Esomchi", "Ezedinma", "Ezeugo", "Ezeobi", "Ezeonwuka", "Ezidinma", "Ezimoha", "Ezurumoke", "Gbujie", "Igboekwu", "Igwenagu",
    "Ihekwoaba", "Ikechukwu", "Ikemefuna", "Ikwuka", "Imeagha", "Imeokpara", "Iroanya", "Iroegbu", "Isinmeme", "Isiugo", "Iweka", "Jibunor", "Katchy", "Kelechi", "Kelechukwu", "Makolo", "Mbamalu", "Mgbemena", "Mgbike", "Mmaduekwe",
    "Mmakwe", "Mmuo", "Mokelu", "Muoekeka", "Ndidi", "Ndubuisi", "Ngonadi", "Nwabuike", "Nwagbara", "Nwagu", "Nwaigwe", "Nwajagu", "Nwakanma", "Nwakibie", "Nwankiti", "Nwanwulu", "Nwatarali", "Nwachinemelu", "Obidiegwu", "Obiegbu",
    
    "Abacha", "Abdallah", "Abdulkadir", "Abubakar", "Adamu", "Aliyu", "Aminu", "Anka", "Atiku", "Bala", "Bello", "Buhari", "Danbaba", "Danladi", "Dantata", "Dasuki", "Dogara", "Ganduje", "Garba", "Gwarzo", "Hadejia", "Haliru", "Haruna", "Idris", "Illela", "Isah", "Jibril", "Jikamshi", 
    "Kabir", "Kaita", "Kano", "Kasimu", "Katagum", "Katsina", "Kawu", "Kazaure", "Kontagora", "Ladan", "Liman", "Madaki", "Mahmoud", "Maigari", "Makarfi", "Malam", "Mallam", "Mamman", "Manga", "Masari", "Mohammed", "Mu'azu",
    "Mustapha", "Nafiu", "Nagogo", "Ningi", "Rano", "Ribadu", "Rijiyar", "Saidu", "Salihu", "Sambo", "Samaila", "Sani", "Shehu", "Sokoto", "Tahir", "Tanimu", "Tijani", "Tukur", "Umaru", "Usman", "Waziri", "Yakubu", "Yamusa", "Yandaki", "Yusuf", "Zubairu", "Zuru", "Zaria", "Zamfara", "Ali",
    "Azare", "Babayo", "Baban", "Bashir", "Danlawan", "Danjuma", "Daura", "Dikko", "Dogo", "Doma", "Galadima", "Gambo", "Gidado", "Gidanjuma", "Hassan", "Hussaini", "Husseini", "Inuwa", "Ismail", "Ibrahim", "Jega", "Kabo", "Kachallah", "Kebbi", "Kura", "Kwasau", "Kwankwaso", "Kwaro", "Lawan", 
    "Lemu", "Makaranta", "Malumfashi", "Mangaji", "Marafa", "Matazu", "Musa", "Musawa", "Nuhu", "Rabo", "Rikoto", "Sabon", "Sama'ila", "Shinkafi", "Tashan", "Tudun", "Tukur-Tukur", "Tsakuwa", "Wali", "Wurno", "Yalwa", "Yelwa", "Yola", "Zaki", "Zango", "Zubair", "Zulfi", "Ahmadu", "Alhassan", 
    "Alkali", "Ammani", "Auta", "Baba", "Bako", "Bashiru", "Birnin", "Bukar", "Bulama", "Bunu", "Burhan", "Dallatu", "Dandume", "DanGote", "Danja", "Dantani", "Dare", "Dawodu", "Faruk", "Funtua", "Gambo", "Garzali", "Gaya", "Goni", "Gujungu", "Habu", "Hafiz", "Haliru", "Hamma", "Harir", 
    "Hashim", "Hunkuyi", "Iliyasu", "Imam", "Ingawa", "Isa", "Jama'are", "Jarmai", "Jatau", "Jega", "Jibir", "Jidda", "Jikamshi", "Jumma", "Jummai", "Kabo", "Kabuga", "Kaduna", "Kaita", "Kalgo", "Kangiwa", "Kari", "Kasimu", "Kibiya", "Kofar", "Kogo", "Kurfi", "Kwami", "Lawan", "Liman", 
    "Madugu", "Maha", "Maidugu", "Maina", "Maishanu", "Mairiga", "Makama", "Mallami", "Maraba", "Marmara", "Masari", "Masud", "Matazu", "Maude", "Mijinyawa", "Modibbo", "Mohammed", "Moktar", "Mukhtar", "Munkaila", "Musa", "Musdafa", "Nafiu", "Nagudu", "Nagwamatse", "Nasiru", "Na'Allah", 
    "Ningi", "Nuhu", "Nura", "Rabiu", "Rafindadi", "Rano", "Rikoto", "Rimi", "Sadiq", "Saheed", "Saidu", "Salihu", "Samaila", "Sani", "Sharif", "Shehu", "Shinkafi", "Shuaibu", "Sokoto", "Sulayman", "Tahir", "Tambari", "Tambuwal", "Tanimu", "Tijjani",
    "Tukur", "Uba", "Umar", "Usaini", "Usman", "Wali", "Wurno", "Yakubu", "Yalwaji", "Yandaki", "Yau", "Yusuf", "Zaharadeen", "Zango", "Zaria", "Zubair", "Zubairu", "Zulfi", "Zuma", "Zurmi", "Danlami", "Danmusa", "Danwanka", "Danzaki", "Dogo", "Gabas", "Gandu", "Gidado", "Gidanjuma", "Gishiri",
    "Gonimi", "Gulma", "Gwadabe", "Gwale", "Gwarzo", "Habu", "Hafiz", "Haliru", "Hanga", "Hunkuyi", "Ibrahim", "Iliyasu", "Ingawa", "Isa", "Ismaila", "Jega", "Jibir", "Jikamshi", "Jidda", "Jumma", "Kabuga", "Kaduna", "Kaita", "Kano", "Katagum", "Kazaure", "Kibiya", "Kofar", "Kogo", "Kurfi",
    "Ladan", "Lemu", "Madugu", "Maina", "Makama", "Marafa", "Masari", "Matazu", "Moktar", "Mukhtar",  "Musdafa", "Nafiu", "Nasiru", "Na'Allah", "Ningi", "Nuhu", "Rabiu", "Rafindadi", "Rano", "Rimi", "Saidu", "Sambo", 
    "Sani", "Shehu", "Sulayman", "Tambuwal", "Tanimu", "Tijjani", "Uba", "Umar", "Usaini", "Wali", "Yakubu", "Yalwaji", "Yandaki", "Yusuf", "Zaharadeen", "Zango", "Zaria", "Zubairu",

    "Abegunde", "Abiodun", "Abiola", "Abiolu", "Abisogun", "Aboderin", "Abodunde", "Abogunrin", "Aboyade", "Abegunde",
    "Adeagbo", "Adebanjo", "Adebayo", "Adebola", "Adebowale", "Adebukunola", "Adebunmi", "Adebunoluwa", "Adebiyi", "Adebisi",
    "Adebusoye", "Adebutu", "Adedapo", "Adedayo", "Adedeji", "Adediran", "Adedoja", "Adedokun", "Adedoyin", "Adeduntan",
    "Adeeko", "Adegbemile", "Adegbesan", "Adegbile", "Adegbite", "Adegbola", "Adegoke", "Adegoroye", "Adegoye", "Adegunde",
    "Adegunwa", "Adegunwa", "Adeigbe", "Adeite", "Adejare", "Adejumobi", "Adejumoke", "Adekanbi", "Adekola", "Adekoya",
    "Adekule", "Adekemi", "Adelabu", "Adelaja", "Adelana", "Adelani", "Adelarin", "Adeleke", "Adelopo", "Adeloye",
    "Adelugba", "Ademola", "Ademoye", "Ademuyiwa", "Adenike", "Adeniran", "Adeniyi", "Adenola", "Adenrele", "Adenuga",
    "Adenusi", "Adeoba", "Adeogun", "Adeola", "Adeolu", "Adeoti", "Aderibigbe", "Aderinsola", "Aderogba", "Aderoju",
    "Aderonke", "Adesanya", "Adesida", "Adesiyan", "Adesoji", "Adesokan", "Adesola", "Adesoye", "Adetokunbo", "Adetola",
    "Adetomiwa", "Adetoro", "Adetoun", "Adetoye", "Adetunji", "Adetuwo", "Adewale", "Adewande", "Adewole", "Adeyanju",
    "Adeyemo", "Adeyeri", "Adeyinka", "Adeyokun", "Adeyolu", "Adeyoyin", "Adeyoyinbo", "Adeyoye", "Adewusi", "Afoke",
    "Afolabi", "Afolayan", "Agbaje", "Agboola", "Ajagbe", "Ajayi", "Akinbode", "Akinboye", "Akinbule", "Akinbuli",
    "Akindele", "Akinfenwa", "Akinjide", "Akinlabi", "Akinleye", "Akinloye", "Akinniyi", "Akinola", "Akinpelu", "Akinremi",
    "Akinsanya", "Akinsehinwa", "Akinsiku", "Akinsola", "Akinsooto", "Akinsowon", "Akinsuyi", "Akinwande", "Akinyemi", "Akinyode",
    "Akinyomi", "Akisanya", "Alade", "Alagbe", "Alarape", "Alaran", "Amoo", "Aremu", "Arinola", "Arisekola",
    "Asabi", "Asimiyu", "Atanda", "Ayantola", "Ayegbajeje", "Ayeni", "Ayoade", "Ayodeji", "Ayodele", "Ayokanmi",
    "Ayokunle", "Ayomide", "Ayoola", "Ayotunde", "Ayowumi", "Babajide", "Babatunde", "Badejo", "Balogun", "Banjo",
    "Banjoko", "Bayode", "Bayonle", "Beecroft", "Bello", "Bisi", "Bolade", "Bolaji", "Bolarinwa", "Boluwaji",
    "Boluwatife", "Borokini", "Bunmi", "Dada", "Damilare", "Damola", "Daramola", "Dauda", "Deji", "Durosinmi",
    "Ebunoluwa", "Ebunoluwakiitan", "Ebunoluwaoluwa", "Ebunoluwaoluwa", "Efunnuga", "Ekundayo", "Elebute", "Eleran", "Emiola", "Emmanuel",
    "Eniola", "Enitan", "Esezobor", "Esin", "Esuola", "Esuruoso", "Fadare", "Fagbemi", "Fagbenro", "Fagbohun",
    "Fagbuyi", "Fakunle", "Fakoya", "Falana", "Faleye", "Falodun", "Falola", "Falomo", "Famakin", "Famakinwa",
    "Famuyiwa", "Faniran", "Fapohunda", "Fasanmi", "Fatogun", "Fatile", "Fatogun", "Fatusin", "Fatuyi", "Fayemi",
    "Fayese", "Fayinka", "Fehintola", "Fehinti", "Feyisetan", "Feyisayo", "Fisayo", "Funmilade", "Funmilayo", "Funmioluwa",
    "Ganiyu", "Gbadamosi", "Gbadebo", "Gbolahan", "Gbonjubola", "Ibikunle", "Ibiyemi", "Idowu", "Ifeoluwa", "Ifeanyichukwu",
    "Ifeoma", "Ifetayo", "Ifewumi", "Igbekele", "Ijaodola", "Ijogun", "Ikuomola", "Ikuotun", "Ilesanmi", "Ilori",
    "Imole", "Ipinlaye", "Iremide", "Iromini", "Iroto", "Isedowo", "Isijola", "Isikalu", "Iyalode", "Iyanda",
    "Iyanuoluwa", "Iyanuwura", "Iyinoluwa", "Jadesola", "Jibola", "Jimoh", "Jokotade", "Jolaade", "Jolaoluwa", "Julius",
    "Kafayat", "Kamardeen", "Karunwi", "Kehinde", "Kenke", "Kikelomo", "Kolade", "Kolapo", "Kolawole", "Komolafe",
    "Kunle", "Labake", "Ladejobi", "Ladele", "Ladipo", "Ladi", "Laitan", "Lanre", "Lasisi", "Layemi",
    "Leye", "Magbagbeola", "Makanju", "Makinde", "Melechukwu", "Morakinyo", "Morenike", "Morenikeji", "Morohunmubo", "Moyinoluwa", 

    "Terkura", "Iorfa", "Orker", "Kwaghbo", "Aondoaver", "Ushakuma", "Aondona", "Terver", "Shija", "Vande",
    "Aondofa", "Jirgba", "Aver", "Terkimbi", "Yima", "Iornem", "Tersoo", "Kohol", "Aondohemba", "Zungwe",
    "Owoicho", "Abah", "Agbo", "Oche", "Edeh", "Adole", "Ochola", "Oketa", "Ikwue", "Onum",
    "Ochanya", "Ogene", "Ejembi", "Ogbole", "Otene", "Aboh", "Ewuga", "Ikande", "Obande", "Ocheje",
    "Aliyu", "Achimugu", "Adegbe", "Amana", "Ocholi", "Itodo", "Onoja", "Agbo", "Okpanachi", "Akwu",
    "Arome", "Enemaku", "Ekele", "Ugbede", "Ohiemi", "Eneyo", "Akoh", "Odoma", "Omale", "Ojoma",
    "Etsu", "Ndako", "Lapai", "Bida", "Kudu", "Yahaya", "Abdullahi", "Gana", "Saba", "Kutigi",
    "Mamman", "Ndagi", "Tsado", "Kure", "Dzukogi", "Gimba", "Wushishi", "Ibrahim", "Mu'azu", "Sani",
    "Adamu", "Dodo", "Gizo", "Egba", "Ebira", "Akawu", "Attah", "Ejini", "Otaru", "Oseni",
    "Salihu", "Obadaki", "Ozugbe", "Ozovehe", "Ohiemi", "Asema", "Ochema", "Ebogwu", "Edegbo", "Enejo",
    "Achor", "Iorhen", "Atsen", "Agishi", "Aga", "Ikyo", "Tiza", "Dooga", "Tarkaa", "Nenge",
    "Jirgba", "Ikyaan", "Shima", "Terna", "Nyitamen", "Torlumun", "Orduen", "Igyese", "Aondofa", "Zua",
    "Yakubu", "Suleiman", "Onazi", "Ibrahim", "Audu", "Okpala", "Usman", "Edache", "Ogbole", "Ejeh",
    "Aku", "Makurdi", "Ochefu", "Ikwue", "Alhassan", "Ekwunife", "Ogbuja", "Aboh", "Agada", "Kudu",
    "Umar", "Useni", "Adaji", "Odoh", "Edogbanya", "Okonkwo", "Ikon", "Okoronkwo", "Enenche", "Nwogbo",
    "Ameh", "Ohinoyi", "Ochigbo", "Adejo", "Obogo", "Atenaga", "Awojo", "Ododo", "Ohinoyi", "Ejini",
    "Onyeke", "Aboh", "Arome", "Ugbede", "Ogwu", "Itoto", "Ejembi", "Alabi", "Ebije", "Sidi",
    "Ndako", "Kano", "Lafia", "Wadata", "Kure", "Gimba", "Zuru", "Tiv", "Akor", "Ekubo",
    "Anka", "Fagbo", "Maikudi", "Dantata", "Olorunfemi", "Azubike", "Eguma", "Yekini", "Igbudu", "Gowon",
    "Kaduna", "Adogo", "Yisa", "Ejoga", "Ibenu", "Tersoo", "Kwaghgba", "Tarkighir", "Orpin", "Azu",
    "Anene", "Aliade", "Mbaduku", "Ogbadibo", "Oba", "Eje", "Ohiani", "Dangana", "Jatau", "Eze",
    "Gbande", "Enenche", "Yisa", "Obande", "Omachi", "Onuh", "Ortum", "Otache", "Dugeri", "Akpoko",
    "Ogwuche", "Ogwiji", "Omachi", "Okenyi", "Atabo", "Ekele", "Ojomale", "Akpa", "Itakpe", "Obekpa",
    "Ojoma", "Ejeh", "Omale", "Ocholi", "Adeku", "Okolo", "Ilemona", "Ochefu", "Idoko", "Ogbeyi",
    "Egbo", "Asema", "Ojotu", "Ojibo", "Ochanya", "Ajume", "Olotu", "Ejule", "Ibukun", "Ajogwu",
    "Alade", "Daramola", "Otinche", "Obiora", "Ojogbane", "Okoh", "Akpulu", "Ajimobi", "Adeyemo", "Okpokwu",
    "Ibanga", "Olubunmi", "Ajayi", "Edogbanya", "Eje", "Atoko", "Ayi", "Ali", "Odumodu", "Ojochide",
    "Ameadaji", "Ebe", "Egalame", "Otabo", "Iliyasu", "Ilori", "Jibrin", "Otimkpu", "Ujah", "Okpala",
    "Amali", "Odobo", "Ejini", "Olatunji", "Bologi", "Ogenyi", "Ogirri", "Ojijoku", "Ojoboh", "Ogijo",
    "Ogotu", "Ezugwu", "Okwueze", "Achor", "Omaga", "Ogboi", "Omale", "Atule", "Ogar", "Ogbuja",
    "Ebibote", "Omara", "Onimisi", "Oshiokpe", "Iren", "Ogoh", "Olatunji", "Adebayo", "Olaolu", "Ajibade",
    "Abiola", "Olanrewaju", "Balogun", "Owolabi", "Ojodu", "Tahir", "Kabir", "Alhaji", "Zamfara", "Kwara",
    "Ajagbe", "Oshagbemi", "Adamu", "Ene", "Onaiyekan", "Idowu", "Ododo", "Akowe", "Omodara", "Oluwale",
    "Gbenga", "Adebanjo", "Otedola", "Omodara", "Odumodu", "Omotosho", "Adebayo", "Olofin", "Olowo", "Ajiboye",

    "Eweka", "Obaseki", "Igbinedion", "Osifo", "Akenzua", "Uhunmwangho", "Ologbosere", "Edebiri", "Eghosa", "Osagie",
    "Omoregie", "Ero", "Omoruyi", "Oyegun", "Ezomon", "Igbinosa", "Ighodaro", "Oboh", "Emovon", "Oviawe",
    "Odiase", "Aisien", "Omoigui", "Okojie", "Agbontaen", "Ikpea", "Eboigbe", "Osunde", "Uwagboe", "Okungbowa",
    "Edebiri", "Iyekowa", "Aghedo", "Osakue", "Ero", "Omoregbe", "Orobator", "Osarumwense", "Eweka", "Uzamere",
    "Onoge", "Egbo", "Uweh", "Odogun", "Aghogho", "Igho", "Efetobore", "Urhobo", "Ejiro", "Tega",
    "Ufuoma", "Oghene", "Esiso", "Uloho", "Oviri", "Erhi", "Oke", "Okiemute", "Omoefe", "Okorodudu",
    "Ebireri", "Egbo", "Akpodiete", "Avwerosuo", "Esimaje", "Akpobome", "Onoyovwi", "Okiemute", "Omajefe", "Akpore",
    "Ogheneovo", "Okagbare", "Erhirhovwe", "Uwhubetine", "Awhinawhi", "Ogbebor", "Ofobrukueta", "Aghogho", "Avwunudiogba", "Obofoni",
    "Omatsola", "Onose", "Ugoji", "Omodu", "Ayibakuro", "Tare", "Preye", "Eremie", "Kemebradikumo", "Seigha",
    "Bariyira", "Alagoa", "Alaowei", "Oki", "Apenu", "Kuro", "Orubibi", "Tamuno", "Bekenawei", "Daba",
    "Egbuson", "Omene", "Akaiso", "Torugbene", "Egbe", "Egberibin", "Azibapu", "Abolarin", "Apere", "Odokuma",
    "Oporoma", "Kalaowei", "Ipigansi", "Doupere", "Ekpetiama", "Boulous", "Kpogbolo", "Ikoli", "Osain", "Opuada",
    "Bara", "Iyakoregha", "Okiro", "Okubama", "Apia", "Nembari", "Biraibo", "Keme", "Timipre", "Ibebe",
    "Wariboko", "Ibim", "Kio", "Wokoma", "Jaja", "Gogo", "Ibama", "Ordu", "Boma", "Dumadei",
    "Inokoba", "Adoki", "Tammy", "Dikibo", "Opusunju", "Kpodoh", "Telema", "Anele", "Opuene", "Kiri",
    "Ateke", "Owunari", "Peremoboere", "Bariyira", "Opusingi", "Wosu", "Ateli", "Alagba", "Benson", "Ofor",
    "Edem", "Itam", "Uko", "Udo", "Bassey", "Ibanga", "Effiom", "Akpan", "Ufot", "Ekpenyong",
    "Essien", "Idim", "Otobong", "Ekanem", "Akpabio", "Eneyo", "Udoenang", "Ikpe", "Abasi", "Udoh",
    "Mkpang", "Unwana", "Ntekim", "Uwana", "Eshiet", "Nse", "Eyo", "Nsien", "Ndiana", "Nsikak",
    "Obong", "Orok", "Udofia", "Eshiet", "Nsikak", "Ikot", "Asuquo", "Uwah", "Akpanke", "Etuk",
    "Ekong", "Umoh", "Udia", "Eshiet", "Eneh", "Ebekpo", "Ituen", "Ufot", "Ebie", "Ikpeme",
    "Ekanem", "Ubot", "Ebong", "Abang", "Udosen", "Orok", "Mkpang", "Mbakara", "Nsima", "Orok",
    "Ukeme", "Nkanta", "Eneh", "Ekop", "Abasiama", "Abia", "Ekpe", "Edim", "Omini", "Ekpenyong",
    "Ita", "Bassey", "Itauma", "Unyime", "Nya", "Ibiang", "Eteng", "Ita", "Ebong", "Odok",
    "Agbor", "Aigbogun", "Ogbemudia", "Osifo", "Eweka", "Ekhorutomwen", "Osemwegie", "Aghedo", "Aigbe", "Asemota",
    "Oduwa", "Igiebor", "Ize-Iyamu", "Oyakhilome", "Oshiomhole", "Odion", "Uzamere", "Omoregie", "Osadolor", "Obasuyi",
    "Edebiri", "Osazuwa", "Okojie", "Igbinosa", "Igbinedion", "Obanor", "Omoruyi", "Odaro", "Uyi", "Okosun",
    "Osakue", "Odigie", "Osawe", "Ogbomo", "Ihaza", "Enabulele", "Igiekhume", "Obiabo", "Ebohon", "Ehigie",

     "Abba", "Aliyu", "Abubakar", "Goni", "Bukar", "Kachallah", "Shettima", "Monguno", "Modu", "Zannah",
    "Dikwa", "Ngala", "Mamman", "Kyari", "Bulama", "Yerima", "Dalori", "Gubio", "Bunu", "Tafida",
    "Guibbu", "Alhaji", "Murtala", "Gamboru", "Kala", "Tukur", "Maigari", "Mustapha", "Kashim", "Bashir",
    "Danbaba", "Khalifa", "Idris", "Saleh", "Garba", "Mai", "Lawan", "Usman", "Adamu", "Modibo",
    "Dawud", "Sanda", "Zubairu", "Faruk", "Jarma", "Kyarimi", "Fugu", "Hajja", "Binta", "Jiddah",
    "Umaru", "Ibrahim", "Yusufari", "Aisami", "Waziri", "Alhassan", "Sadiq", "Dankaka", "Makinta", "Haruna",
    "Sanda", "Bunu", "Bakura", "Murtala", "Hussaini", "Jalo", "Ba'aba", "Bappa", "Mohammed", "Balarabe",
    "Danlami", "Gidado", "Gadzama", "Iliya", "Babba", "Yerima", "Fannami", "Ngulde", "Ajayi", "Chinda",
    "Ibrahim", "Ngurdo", "Muktar", "Dankaka", "Wakil", "Hamma", "Bashir", "Talba", "Danjuma", "Sulaiman",
    "Tanimu", "Abacha", "Gambo", "Saidu", "Tasiu", "Murtala", "Ali", "Hauwa", "Fatima", "Sa'idu",
    "Ismail", "Malam", "Musa", "Bukar", "Shuwa", "Kachalla", "Dogo", "Dantani", "Maina", "Bulus",
    "Maikudi", "Kaloma", "Bappah", "Maidugu", "Shagari", "Kasimu", "Tukur", "Dikwa", "Liman", "Danladi",
    "Maikano", "Buwai", "Fannami", "Dalhatu", "Waziri", "Audu", "Anas", "Gargari", "Dauda", "Dankani",
    "Habu", "Maidawa", "Malam", "Tsoho", "Baba", "Jauro", "Mahdi", "Maidoki", "Kabo", "Mairiga",
    "Hassan", "Yahaya", "Maigida", "Gwoza", "Bachama", "Kilba", "Margi", "Bura", "Tera", "Yobe",
    "Fika", "Fune", "Gujba", "Nguru", "Jajere", "Damaturu", "Mungono", "Askira", "Biu", "Bayo",
    "Garkida", "Kwaya", "Kukawa", "Nganzai", "Shani", "Gombi", "Hong", "Jada", "Mayo", "Tafawa",
    "Balewa", "Darazo", "Ganjuwa", "Misau", "Katagum", "Jama'are", "Itas", "Warji", "Kirfi", "Ningi",
    "Gamawa", "Gashua", "Nguru", "Bade", "Machina", "Geidam", "Yusufari", "Jakusko", "Fune", "Fika",
    "Potiskum", "Gujba", "Damaturu", "Nguru", "Gashua", "Buni", "Gulani", "Tarmuwa", "Biu", "Bayo",
    "Hawul", "Kwaya", "Shani", "Gombe", "Akko", "Yamaltu", "Deba", "Funakaye", "Kwami", "Nafada",
    "Dukku", "Balanga", "Shongom", "Billiri", "Kaltungo", "Yalmatu", "Kwami", "Dukku", "Akko", "Funakaye",
    "Warji", "Gwaram", "Dass", "Bauchi", "Ganjuwa", "Misau", "Bogoro", "Tafawa", "Balewa", "Darazo",
    "Alkaleri", "Toro", "Kirfi", "Warji", "Itas", "Jama'are", "Zaki", "Gamawa", "Shira", "Dambam",
    "Ningi", "Azare", "Misau", "Katagum", "Itas", "Ganjuwa", "Jama'are", "Bogoro", "Dass", "Bauchi",
    "Darazo", "Alkaleri", "Warji", "Shira", "Dambam", "Gamawa", "Zaki", "Gwaram", "Toro", "Kirfi",
    "Ningi", "Azare", "Misau", "Katagum", "Shani", "Damboa", "Chibok", "Askira", "Uba", "Gombi",
    "Hong", "Mubi", "Maiha", "Michika", "Madagali", "Song", "Girei", "Fufore", "Yola", "Njoboliyo",
    "Demsa", "Numan", "Shelleng", "Guyuk", "Lamurde", "Mayo", "Belwa", "Jada", "Ganye", "Toungo",
    "Gashaka", "Serti", "Takum", "Wukari", "Ibi", "Donga", "Lau", "Ardo", "Kola", "Bali",
    "Gassol", "Kurmi", "Sardauna", "Ussa", "Yorro", "Zing", "Yola", "Gombi", "Hong", "Mubi",
    "Maiha", "Michika", "Madagali", "Song", "Girei", "Fufore", "Yola", "Demsa", "Numan", "Shelleng",
    "Guyuk", "Lamurde", "Jada", "Ganye", "Toungo", "Gashaka", "Serti", "Takum", "Wukari", "Ibi",
    "Donga", "Lau", "Bali", "Gassol", "Kurmi", "Sardauna", "Ussa", "Yorro", "Zing", "Ganye"

]
        return self.random_element(surnames)
    
class FirstNameByGender(BaseProvider):
    def male_name(self):
        boys = ["Chukwudi", "Obinna", "Ifeanyi", "Chinedu", "Emeka", "Uchenna", "Chijioke", "Tochukwu", "Chisom", "Ekene",
        "Chibuzo", "Okechukwu", "Onyeka", "Kelechi", "Izuchukwu", "Chukwuemeka", "Chukwuma", "Nonso", "Somtochukwu", "Eze",
        "Chigozie", "Obiora", "Ugochukwu", "Okwudili", "Osondu", "Ozoemena", "Uzochukwu", "Ejike", "Odinaka", "Ekenedilichukwu",
        "Nnaemeka", "Ikenna", "Ugo", "Chibuike", "Ogechukwu", "Chinonso", "Chukwuka", "Echezona", "Ebubechukwu", "Nwachukwu",
        "Chibuikem", "Somadina", "Chukwuemelie", "Ifechukwu", "Jidenna", "Odumegwu", "Udochukwu", "Chukwudiebube", "Ezinna", "Obioma",
        "Chidubem", "Uchennaemeka", "Chinagorom", "Chukwunyelum", "Echezonachukwu", "Olamma", "Chukwuebuka", "Nwokeoma", "Ezeugo", "Ekwefi",
        "Afamefuna", "Onyekachi", "Anyanwu", "Ekenedilichukwu", "Onochie", "Ekwueme", "Okonkwo", "Amadi", "Ukaegbu", "Nwafor",
        "Chibundu", "Chimezie", "Uche", "Chukwuebube", "Nnamdi", "Obi", "Ekwutosinam", "Chinwe", "Chidinazo", "Zimuzo",
        "Chukwumezie", "Zikomo", "Chukwudera", "Ekwealor", "Muna", "Chinaka", "Onwa", "Dike", "Uzochukwu", "Ifenna",
        "Uzondu", "Ebube", "Chibuokem", "Obiorah", "Echezona", "Chimeka", "Eziama", "Oziomachukwu", "Onochukwu", "Nzube",
        "Maduabuchi", "Ikenwa", "Afam", "Chiemela", "Obiageri", "Ihuanuzo", "Ikechukwu", "Onyedikachi", "Chinualumogu", "Obieze",
        "Chukwujekwu", "Ifezue", "Ozor", "Ezeudo", "Chikwado", "Akachi", "Ezeibe", "Chibundum", "Chiemezie", "Chukwukadibia",
        "Ekwekwuo", "Ozoemenam", "Nzubem", "Chinonyelum", "Obiageri", "Chizirim", "Chukwualuka", "Ekelem", "Okwuchukwu", "Omekannaya",
        "Chijiokem", "Obiekwe", "Omenanwafor", "Chikwuma", "Onyekwere", "Nduka", "Okechukwum", "Uchenwam", "Ekenechukwu",
        "Obiageri", "Ozoemela", "Chiziterem", "Uchenwamaka", "Onwuka", "Nnamso", "Okwuma", "Eziaku", "Nnabugwu", 
        "Uchenwanne", "Chisombiri", "Chigozirim", "Obinnaemeka", "Chibundu", "Obinna", "Okwudili", "Nnamdi", "Azubuike", "Echezona", "Kamsiyochukwu", "Chidera", 
        "Chijoke", "Chinaza", "Olisaemeka", "Chuka", "Chimdindu", "Onyedika",
        "Abba", "Abdullahi", "Abubakar", "Adamu", "Aliyu", "Aminu", "Balarabe", "Bello", "Danjuma", "Faruk",
        "Gambo", "Garba", "Habibu", "Hafizu", "Hassan", "Ibrahim", "Idris", "Isah", "Jamilu", "Kabiru",
        "Kamal", "Kasim", "Lawal", "Mahmoud", "Malam", "Mamman", "Musa", "Mustapha", "Nuhu", "Rabi’u",
        "Sadiq", "Salihu", "Shehu", "Shuaibu", "Suleiman", "Tahir", "Tanko", "Umar", "Usman", "Yakubu",
        "Yahaya", "Zubairu", "Ali", "Bashir", "Dahiru", "Haruna", "Jibril", "Khalid", "Lukman", "Nasir",
        "Sabo", "Ubaidullah", "Zayyanu", "Muntari", "Tijjani", "Sa’ad", "Danladi", "Balarabe", "Rabiu",
        "Tasi’u", "Ilyasu", "Hamisu", "Ismaila", "Dauda", "Gidado", "Sa’idu", "Maikudi", "Gwarzo", "Ahmadu",
        "Waziri", "Magaji", "Abdulkadir", "Basiru", "Sarkin", "Mahadi", "Ado", "Danjuma", "Sule", "Nagudu",
        "Iliyasu", "Hafiz", "Muktar", "Habibu", "Maikano", "Nasiru", "Tukur", "Babagana", "Gaddafi", "Babangida",
        "Magawata", "Danjuma", "Abdulmajid", "Abdulfatai", "Sanda", "Danbaba", "Muhammadu", "Katsina", "Buhari", "Gwabro",
        "Gambo", "Ahmed", "Madaki", "Dogo", "Dankwambo", "Zaki", "Yakubu", "Salisu", "Jallo", "Alhaji",
        "Sarkin", "Jama’are", "Adamu", "Hussaini", "Murtala", "Jega", "Uba", "Danlami", "Kawu", "Yushau",
        "Tahir", "Sadi", "Gidado", "Ali", "Muhajir", "Sadisu", "Suleiman", "Idris",
        "Ibrahim", "Isa", "Bashir", "Balarabe", "Shagari", "Tanimu", "Tanko", "Ado", "Shettima", "Gambo",
        "Goni", "Zainu", "Kabir", "Saidu", "Bashiru", "Liman",
        "Danlami", "Hudu", "Dikko", "Faruk", "Tudun", "Babayo", "Isma’il", "Murtada",
        "Ade", "Adebayo", "Adejare", "Adejumo", "Adeniyi", "Adeola", "Aderemi", "Adesina", "Adetayo", "Adetokunbo",
        "Adetola", "Adetunji", "Adewale", "Adewumi", "Afolabi", "Ajibola", "Akin", "Akintayo", "Akinwumi", "Ayinde",
        "Ayobami", "Ayodeji", "Ayoola", "Ayotunde", "Babajide", "Babatunde", "Bolaji", "Damilare", "Damilola", "Darasimi",
        "Dotun", "Ebunoluwa", "Egbeyemi", "Ekundayo", "Femi", "Feyisayo", "Folahan", "Goke", "Idowu", "Ifedayo",
        "Ifeoluwa", "Ilesanmi", "Iremide", "Ishola", "Itunuoluwa", "Jadesola", "Jibola", "Kazeem", "Kolapo", "Kolawole",
        "Kunle", "Lekan", "Makanjuola", "Mayowa", "Mobolaji", "Modupe", "Mofe", "Mojisola", "Morakinyo", "Muyiwa",
        "Niyi", "Oladapo", "Oladimeji", "Oladiran", "Oladokun", "Olalekan", "Olanrewaju", "Olasunkanmi", "Olumide", "Oluwafemi",
        "Oluwasegun", "Oluwaseun", "Oluwatobi", "Oluwatofunmi", "Oluwatomiwa", "Oluwatoyin", "Omotayo", "Opeyemi", "Oreoluwa", "Otito",
        "Segun", "Seyi", "Shina", "Taiwo", "Temidayo", "Toba", "Tope", "Tosin", "Tunji", "Wale",
        "Yemi", "Yewande", "Yewole", "Yomi", "Yusuf", "Zacchaeus", "Ajayi", "Alade", "Aderogba", "Adenuga",
        "Adeyemi", "Ajagun", "Akinpelu", "Akinwande", "Akinwale", "Akingbade", "Ayodele", "Bankole", "Bayode", "Bolarinwa",
        "Durojaiye", "Esubiyi", "Fagbohun", "Fagbemi", "Fadeyi", "Igbekele", "Ipinlaye", "Isola", "Jokotade", "Kehinde",
        "Mobolanle", "Morounkeji", "Olumuyiwa", "Opeyemi", "Osanyin", "Oyewole", "Oyinlola", "Sijuade", "Sulaimon", "Tijani",
        "Tokunbo", "Tosin", "Wasiu", "Yewande", "Yetunde", "Abioye", "Abiara", "Abolaji", "Adebisi", 
        "Abah", "Abaji", "Adaji", "Adanu", "Adingi", "Afa", "Audu", "Avese", "Aver", "Azubuike",
        "Bem", "Bunu", "Chado", "Dajo", "Danladi", "Danjuma", "Dondo", "Ebije", "Edeh", "Egbunu",
        "Ejiga", "Ejima", "Ejogwu", "Ekele", "Eli", "Emmanuel", "Emodogo", "Eneji", "Ezekiel", "Gadzama",
        "Gado", "Garaku", "Goke", "Gulu", "Gyang", "Idoko", "Igoche", "Igwe", "Ikani", "Iliya",
        "Inalegwu", "Isa", "Ismaila", "Itodo", "Jacob", "Jibrin", "Joshua", "Julius", "Kaigama", "Katsina",
        "Kolo", "Kwaghfan", "Kwaghkwah", "Kwaghzer", "Lami", "Liman", "Lokongoma", "Madugu", "Mahmood", "Makama",
        "Mangu", "Mashat", "Mason", "Mathias", "Mohammed", "Moses", "Musa", "Naphtali", "Nathaniel", "Ngbede",
        "Oche", "Ocholi", "Ogbole", "Ogwuche", "Ojo", "Okeke", "Oko", "Okopi", "Okpanachi", "Okpe",
        "Onuche", "Onyilo", "Oodo", "Orokam", "Orume", "Oseni", "Osu", "Owoicho", "Paul", "Peter",
        "Saater", "Saawuan", "Samaila", "Samson", "Sarki", "Shaibu", "Shagari", "Shamaki", "Shekwolo", "Tajudeen", "Tanko", "Tarkighir", "Terhemen", "Terna", "Terngu", "Tersoo", "Timothy", "Tiza",
        "Ujah", "Ujor", "Usman", "Victor", "Yakubu", "Yankari", "Yohana", "Yohanna", "Zachariah", "Zubairu",
        "Abam", "Abasi", "Abasiofon", "Abasiodiong", "Abayomi", "Abednego", "Abiemo", "Abrakasa", "Abugewa", "Adaka",
        "Adanoritsewo", "Adeseun", "Adukpo", "Agbamu", "Aginighan", "Aghogho", "Airelobhegbe", "Aisagbonhi", "Akaba", "Akani",
        "Akpabio", "Akpe", "Akpevwe", "Akpor", "Akporode", "Akpos", "Akpoviri", "Alagbariya", "Alakowe", "Amas",
        "Amasike", "Amasou", "Anari", "Anebode", "Anes", "Anietie", "Anighoro", "Anikwe", "Arhuanran", "Asagba",
        "Asawa", "Atigbi", "Atsegbua", "Atuanya", "Awhinawhi", "Awotiri", "Awotwe", "Azubuike", "Bamuza", "Bawa",
        "Benibo", "Boroh", "Boro", "Bosah", "Boye", "Breson", "Bumie", "Cletus", "Dabo", "Dafe",
        "Dafinone", "Dami", "Danjuma", "Dapiri", "Dason", "Davidson", "Demehin", "Diepreye", "Dikio", "Dimieari",
        "Dinma", "Douye", "Dukebede", "Dukok", "Dumebi", "Dumo", "Durojaiye", "Duwara", "Ebifowei", "Ebikabowei",
        "Ebikere", "Ebikoro", "Ebirikoma", "Ebunoluwa", "Efetobore", "Egbema", "Egbogho", "Ebisike", "Ebun", "Edafe",
        "Edidiong", "Efe", "Efemena", "Efiye", "Ekanem", "Ekpen", "Ekpenga", "Elohor", "Emaye", "Emene",
        "Emwanta", "Enoma", "Erebor", "Eseoghene", "Etokebe", "Etomuko", "Etumudor", "Eurere", "Ewoma", "Eyituoyo", 
        "Abacha", "Abba", "Abdallah", "Abdulkadir", "Abdullahi", "Abubakar", "Adamu", "Aliyu", "Audu", "Babakura",
        "Bako", "Barde", "Bashir", "Buba", "Bukar", "Bulama", "Danjuma", "Dawud", "Faruk", "Gambo",
        "Goni", "Gwaza", "Habu", "Hadi", "Hajara", "Hussaini", "Ibrahim", "Idris", "Isah", "Jafaru",
        "Jauro", "Kaigama", "Kalli", "Kawu", "Kolo", "Kyari", "Lawan", "Madaki", "Mahmoud", "Mamman",
        "Modu", "Mohammed", "Muktar", "Mustapha", "Nafiu", "Nasiru", "Ndahi", "Ndume", "Rabiu", "Ramat",
        "Ruqayyah", "Sa'ad", "Saidu", "Salihu", "Sanda", "Shehu", "Shuaibu", "Suleiman", "Tafida", "Tanimu",
        "Umar", "Usman", "Wakili", "Yakubu", "Yalwa", "Yusuf", "Zain", "Zannah", "Zubairu", "Zurfi",
        "Alhaji", "Ali", "Aminu", "Auwal", "Barde", "Bashiru", "Bawa", "Bawa-Allah", "Dikko", "Dogo",
        "Garba", "Gidado", "Gidari", "Gidari-Waza", "Gubio", "Habibu", "Hajara", "Hussain", "Inuwa", "Isa",
        "Jarma", "Jatau", "Jibir", "Jiddah", "Jikan", "Joda", "Kabiru", "Kaka", "Kashim", "Kurfi"

        
    ]
        return self.random_element(boys)

    def female_name(self):
        girls = ["Amarachi", "Chiamaka", "Chidinma", "Adanna", "Ngozi", "Chizoba", "Ifunanya", "Oluchi", "Ogechi", "Nneka",
        "Chinelo", "Onyinyechi", "Somtochukwu", "Chikaodili", "Obianuju", "Ebere", "Chinyere", "Ugonma", "Nwanyibuife", "Ihuoma",
        "Chisimdi", "Uzoamaka", "Ezinne", "Chigozirim", "Adaugo", "Munachimso", "Chimamanda", "Ijeoma", "Ozioma", "Chinenye",
        "Ifesinachi", "Osinachi", "Uchechi", "Nkeiru", "Omalicha", "Ekwutosi", "Nkiruka", "Amaka", "Obiageli", "Anwuli",
        "Nwanyieze", "Nwabundo", "Mmasinachi", "Ebelechukwu", "Ginika", "Nmesomachukwu", "Onyinye", "Ucheoma", "Ifediora", "Akudo",
        "Ogechinyere", "Omalinze", "Chidinanu", "Ngozichukwu", "Munachi", "Ezichi", "Uchechukwu", "Chinagorom", "Oziomachukwu", "Nneoma",
        "Obialor", "Chiazokam", "Okwuosa", "Omenka", "Chisomebi", "Nwaoma", "Chizitelu", "Ozioma", "Chisombiri", "Obiageri",
        "Nwanyibunwa", "Echefu", "Egwuekwe", "Ekweozor", "Omenala", "Maduako", "Ejiamatu", "Ekwealor", "Chibundun", "Omenkannaya",
        "Chiziterem", "Nzubechi", "Ugochinyere", "Chinwe", "Onwuma", "Echem", "Ositadimma", "Ifebuche", "Chukwumaeze", "Echem",
        "Echem", "Eziaku", "Ihueze", "Ekwuozor", "Nwachinemelu", "Uchechukwu", "Omenkanwa", "Onyinyechukwu", "Eziama", "Nkechi",
        "Ebele", "Ezinne", "Ekemma", "Nwando", "Adaeze", "Adaobi", "Nneoma", "Nwanneka", "Chiamaka", "Uchechi",
        "Nneka", "Oluchi", "Nkeiru", "Ebelechukwu", "Omalicha", "Nwanyieze", "Mmasinachi", "Onyinye", "Ucheoma", "Akudo",
        "Aisha", "Zainab", "Hafsat", "Fatima", "Maryam", "Khadija", "Asiya", "Jamila", "Sadiya", "Halima",
        "Aminat", "Bilqis", "Rukayya", "Safiya", "Firdausi", "Hauwa", "Sakina", "Samira", "Aminatu", "Lubna",
        "Hadiza", "Nafisa", "Rahama", "Zuwaira", "Maimuna", "Shafa’atu", "Hajara", "Surayya", "Husna", "Aisha’u",
        "Asabe", "Rabi", "Lami", "Habiba", "Fati", "Yalwa", "Iya", "Binta", "Goggon", "Salamat",
        "Hafiza", "Sufiya", "Mariya", "Raliya", "Zulaiha", "Sa’adatu", "Munira", "Fiddausi", "Ladidi", "Zaliha",
        "A’isha", "Na’ima", "Mubina", "Jemila", "Sakinatu", "Wasila", "Zahra", "Adama", "Bilqees", "Hadiza",
        "Gimbiya", "Nusaiba", "Nana", "Hajara", "Goggon", "Hadiza", "Salima", "Yayari", "Sabrina", "Rahma",
        "Saliha", "Saudatu", "Zuwaira", "Zuwaitu", "Ummi", "Mimuna", "Barira", "Aminatu", "Gaddo", "Inna",
        "Jibirya", "Mujahidat", "Hannatu", "Tajuddeen", "Rukkayya", "Shafaat", "Shafau", "Yusra", "Saida", "Rashida",
        "Talle", "Dije", "Karima", "Shakira", "Fatimah", "Asmau", "Hindatu", "Ikrama", "Bilkisu", "Halimat",
        "Rabia", "Latifat", "Lubabatu", "Sa’adatu", "Jibrila", "Nafisatu", "Samiratu", "Mufidatu", "Salimatu", "Kauthar",
        "Siti", "Hawwa", "Rabi’a", "Sa’idu", "Mufida", "Yasirat", "Sariatu", "Rahimatu", "Fawziyat", "Hadizat",
        "Najaatu", "Bintou", "Hadizatou", "Isma’ila", "Zubaida", "Ladida", "Dawodu", "Rufaida", "Rahmanatu", "Rahmatu",
        "Rasha", "Sufiyya", "Lami", "Yelwa", "Baturiya", "Kulu", "Saharatu", "Habibat", "Fawziya", "Husnatu",
        "Fariyat", "Imanatu", "Hassana", "Jemilatu", "Faridatu", "Saudatu", "Bilqisu", "Wasilat", "Latifatu", "Aminatu", 
        "Adebimpe", "Adebukola", "Adebola", "Adedoyin", "Adedun", "Adeduntan", "Adejoke", "Adejumo", "Adekemi",
        "Adekoya", "Adekunbi", "Adelomo", "Ademide", "Adenike", "Aderonke", "Aderunke", "Adesewa", "Adetoke", "Adetoun",
        "Adetutu", "Adeyemi", "Adeyinka", "Aderinsola", "Ajoke", "Anjola", "Anuoluwapo", "Arike", "Ayobisi", "Ayokunle",
        "Ayomide", "Ayomikun", "Ayotomiwa", "Ayotunde", "Bolatito", "Bukola", "Busayo", "Damilola", "Darasimi", "Dolapo",
        "Dupe", "Ebun", "Ebunoluwa", "Eriyomi", "Ewaoluwa", "Fadekemi", "Feyikemi", "Feyisayo", "Folake", "Folashade",
        "Funmilayo", "Ibukunoluwa", "Ibidun", "Ibironke", "Idunnu", "Ifedolapo", "Ifedunni", "Ifedayo", "Ifetayo", "Ifeoluwa",
        "Ifeoluwapo", "Igbagbo", "Ire", "Iremide", "Iretomiwa", "Iretioluwa", "Iyanuoluwa", "Jadesola", "Joke", "Jolaade",
        "Kemi", "Kikelomo", "Mofifunoluwa", "Mojisola", "Modupe", "Morounke", "Morounfolu", "Morounkeji", "Morohunmubo", "Moyosoreoluwa",
        "Motunrayo", "Moyinoluwa", "Mubo", "Nifemi", "Olamide", "Oluwadamilola", "Oluwadunmininu", "Oluwafikayomi", "Oluwafolake", "Oluwajomiloju",
        "Oluwakemi", "Oluwakorede", "Oluwatamilore", "Oluwateniola", "Oluwatimilehin", "Omobolanle", "Omobonike", "Omobonoluwa", "Omoboriola", "Omofolake",
        "Omoteniola", "Omowunmi", "Opeyemi", "Oreoluwa", "Oyinlola", "Oyindamola", "Remilekun", "Sade", "Simisola", "Sunkanmi",
        "Temidayo", "Temiloluwa", "Temitayo", "Titilayo", "Tolulope", "Tomiwa", "Tosin", "Yetunde", "Yewande", "Zainab", 
        "Abasiodiong", "Abidemi", "Adesuwa", "Adolor", "Aduke", "Agbonifo", "Agofure", "Agum", "Aimasiko", "Airi",
        "Akasieme", "Akevwese", "Akhimien", "Akintunde", "Alaere", "Alohan", "Amafini", "Amalime", "Amayeseigha", "Amasuo",
        "Amatu", "Amayo", "Anene", "Anokpe", "Anulu", "Anwuli", "Anya", "Aphika", "Apere", "Apreku",
        "Arimiyaw", "Aroghene", "Asemota", "Asoro", "Atiti", "Atupere", "Awani", "Awoko", "Ayeabeni", "Ayiri",
        "Bameyi", "Bebi", "Benedicta", "Bessan", "Bezi", "Bie", "Blessing", "Bolanle", "Borokini", "Bosede",
        "Budu", "Bunmi", "Bussie", "Chikodiri", "Chinyere", "Daibo", "Dame", "Damei", "Daniela", "Deborah",
        "Dibofa", "Dikidi", "Dimafeli", "Dinyefa", "Diseye", "Dolapo", "Dunmininu", "Ebikaboere", "Ebike", "Ebitari",
        "Ebitimi", "Ebos", "Ebra", "Ebruba", "Ebulanu", "Echofe", "Ededjumo", "Edewor", "Edidem", "Ediri",
        "Efeoghene", "Efeturi", "Efetobo", "Efobi", "Ekanem", "Ekpe", "Ekpedeme", "Ekpoti", "Elozino", "Emanuela",
        "Emuejevoke", "Emuesiri", "Emurotu", "Enakhe", "Enebeli", "Enemakpor", "Enemuo", "Ere", "Erejuwa", "Eselemo",
        "Aisha", "Amina", "Asabe", "Balkisu", "Bintu", "Bishara", "Bola", "Fadimatu", "Fatima", "Fiddausi",
        "Hadiza", "Hafsat", "Hauwa", "Hauwa'u", "Hawanatu", "Jamila", "Jummai", "Kaltume", "Khadija", "Laraba",
        "Lami", "Lantana", "Lawanatu", "Maryam", "Maimuna", "Mariya", "Nana", "Na'ima", "Rabi", "Rahila",
        "Ramat", "Rashida", "Rukayya", "Sa'adatu", "Sadiya", "Salma", "Samira", "Sefinat", "Sekina", "Shafa'atu",
        "Sumayya", "Suraiya", "Talle", "Tantile", "Titi", "Umma", "Ummulkhairi", "Yagana", "Yalwa", "Zahra",
        "Zainab", "Zulaihat", "Ajaratu", "Anisa", "Arifa", "Asiya", "Asmau", "Aziza", "Barira", "Bilqis",
        "Budur", "Bushra", "Duniya", "Fauziyya", "Farida", "Ganiyat", "Halimatu", "Hameeda", "Hasana", "Hayatu",
        "Husna", "Ilham", "Iman", "Inaya", "Janna", "Kadija", "Kamila", "Karima", "Liyana", "Lubna",
        "Mansura", "Marwa", "Mashkurah", "Mawada", "Miskina", "Mubina", "Munira", "Muskina", "Nasiba", "Najaatu",
        "Najat", "Nusayba", "Qamar", "Rahama", "Rayhana", "Rihana", "Sabira", "Sakinatu", "Salsabila", "Samirat"
        ]
        return self.random_element(girls)
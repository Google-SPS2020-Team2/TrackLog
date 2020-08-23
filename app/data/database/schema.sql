DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS music;
DROP TABLE IF EXISTS artist;
DROP TABLE IF EXISTS practice;

CREATE TABLE IF NOT EXISTS user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  nickname TEXT NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS  music (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  music_name TEXT NOT NULL,
  artist_id INTEGER,
  difficulty INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS  artist (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  artist_name TEXT NOT NULL,
  introduction TEXT
);

CREATE TABLE IF NOT EXISTS  favourite (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  music_id INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS  practice (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  music_id INTEGER NOT NULL,
  player_id INTEGER NOT NULL,
  score INTEGER NOT NULL DEFAULT 0,
  content TEXT,
  FOREIGN KEY (music_id) REFERENCES music (id),
  FOREIGN KEY (player_id) REFERENCES user (id)
);

INSERT INTO artist (artist_name, introduction) VALUES ('Yundi Li', '李云迪（1982年10月7日－），曾用名李希、李希熙，重庆人，中国钢琴家。李云迪2000年在第十四届肖邦国际钢琴比赛中获得金奖，成为有史以来最年轻的获奖者。2001年，首次登上央视春晚舞台；同年，他与环球唱片公司旗下品牌德意志留声机公司（DG）签订唱片合约，成为首位与DG签约的华人钢琴家并发行首张古典音乐专辑《肖邦精选》。2002年，李云迪发行专辑《李斯特钢琴精选集》，该专辑获得德国回声音乐古典奖和《纽约时报》年度唱片奖。同时发行的还有《安可精选集》。2003年发行了首张自传式精选大碟《Portrait》。2004年发行了首张演奏会DVD《巴登独奏会》并发行了专辑《肖邦诙谐曲和即兴曲集》。2005年发行了专辑《乐聚维也纳》。2007年，发行了《肖邦/李斯特第一钢琴协奏曲》并被企鹅唱片指南评定为四星加钥匙及三星，7月李云迪与小泽征尔及柏林爱乐合作并发行专辑《乐动柏林》。2010年与DG合约到期终止后，李云迪转签EMI并发行了专辑《肖邦夜曲》及《北京独奏会》，同年，李云迪获得波兰政府颁发的“荣耀艺术”文化勋章和第一份“肖邦护照”。2011年发行了专辑《红色钢琴》。2012年，李云迪与环球唱片公司再次签约，重返DG，并推出新唱片《贝多芬:悲怆·月光·热情》。2014年，发行专辑《王者幻想》。2015年9月，发行专辑《肖邦传奇》；10月，受邀担任第17届肖邦国际钢琴比赛评委。2016年，李云迪推出专辑《肖邦：叙事曲》，并在北美、亚欧等地陆续进行多场巡演。2017年5月，李云迪的个人艺术馆在重庆黄桷坪钢琴博物馆开幕，8月进行了与华沙爱乐乐团合作的首次自弹自指巡演，11月与德累斯顿萨克森国立乐团进行了合作巡演。2018年2月，李云迪第四次登上中央电视台春节联欢晚会舞台，表演了钢琴协奏曲《黄河颂》，4月，作为青年代表受邀出席《2018博鳌亚洲论坛》并在“博鳌之夜”主题晚宴表演。自6月起，展开“云指肖邦”世界巡演。');

INSERT INTO artist (artist_name, introduction) VALUES ('Lang Lang', '郎朗（1982年6月14日－），满族，满洲钮祜禄氏，辽宁沈阳人，中国钢琴家。他曾被数家美国权威媒体称作“当今这个时代最天才、最闪亮的偶像明星”，他是受聘于世界顶级的柏林爱乐乐团和美国五大交响乐团的第一位中国钢琴家。曾被《人物（青年版）》杂志称为“将改变世界的20名青年”之一。现居美国纽约。');

INSERT INTO artist (artist_name, introduction) VALUES ('Beethoven', '贝多芬（1982年6月14日－），德意志作曲家、钢琴演奏家。贝多芬上承古典乐派传统，下启浪漫乐派之风格与精神，因而在音乐史上占有非常重要的地位。自1814年开始他的听力急剧下降，于是放弃了钢琴演奏和指挥，但却坚持创作。贝多芬一生共创作了9首编号交响曲、36首钢琴奏鸣曲（其中32首带有编号，1首未完成）、10部小提琴奏鸣曲、16首弦乐四重奏、1部歌剧及2部弥撒曲等等。这些作品对音乐发展有着深远影响。');

INSERT INTO artist (artist_name, introduction) VALUES ('Mozart', '莫扎特（1756年1月27日－1791年12月5日），古典时期的作曲家及钢琴家。莫扎特是位多产的作曲家，一生创作了600多部作品，几乎涵盖所有形式体裁，他在短暂的生命里将古典时期的音乐风格臻于成熟并发扬光大，其作品也被广泛视为古典音乐的典型，对后世有极大的影响。');

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Colourful Clouds Chasing The Moon', 1, 3);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Chopin: Scherzo No.2 in B flat minor, Op.31', 1, 3);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Hungarian Rhapsody', 2, 3);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Andante spianato and Grande polonaise, Op. 22: Andante spianato', 2, 4);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Fate Symphony', 3, 3);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Symphony No. 9 in D minor, Op. 125', 3, 5);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Minuet and Trio in G', 4, 4);

INSERT INTO music (music_name, artist_id, difficulty) VALUES ('Requiem aeternam', 4, 4);


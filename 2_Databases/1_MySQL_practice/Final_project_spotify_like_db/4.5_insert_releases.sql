use spotify;

-- inserting 300 releases with randomly generated data

insert into releases (title, image_file_link, type) values ('Life Partners', 'http://dummyimage.com/165x171.jpg/dddddd/000000', 'EP'),
	('Held Up', 'http://dummyimage.com/210x196.png/cc0000/ffffff', 'single'),
	('Gozu (Gokudô kyôfu dai-gekijô: Gozu)', 'http://dummyimage.com/153x130.jpg/dddddd/000000', 'EP'),
	('35 Up', 'http://dummyimage.com/198x185.png/ff4444/ffffff', 'album'),
	('German Doctor, The (Wakolda)', 'http://dummyimage.com/145x227.jpg/dddddd/000000', 'single'),
	('Last Orders', 'http://dummyimage.com/101x131.png/cc0000/ffffff', 'single'),
	('Coffee Town', 'http://dummyimage.com/174x150.bmp/ff4444/ffffff', 'EP'),
	('Shopworn Angel, The', 'http://dummyimage.com/204x224.jpg/dddddd/000000', 'EP'),
	('Sauna', 'http://dummyimage.com/179x184.bmp/5fa2dd/ffffff', 'album'),
	('Doghouse', 'http://dummyimage.com/130x137.jpg/5fa2dd/ffffff', 'album'),
	('Chamber, The', 'http://dummyimage.com/102x249.bmp/5fa2dd/ffffff', 'single'),
	('Antoine and Colette (Antoine et Colette)', 'http://dummyimage.com/154x239.jpg/dddddd/000000', 'single'),
	('Bobby Deerfield', 'http://dummyimage.com/246x115.png/cc0000/ffffff', 'EP'),
	('I giorni contati', 'http://dummyimage.com/156x102.jpg/ff4444/ffffff', 'single'),
	('Record of a Tenement Gentleman (Nagaya shinshiroku)', 'http://dummyimage.com/227x202.bmp/cc0000/ffffff', 'single'),
	('Dimples', 'http://dummyimage.com/247x178.jpg/dddddd/000000', 'album'),
	('If Looks Could Kill', 'http://dummyimage.com/166x154.bmp/ff4444/ffffff', 'album'),
	('Dandelion', 'http://dummyimage.com/161x246.bmp/cc0000/ffffff', 'EP'),
	('Angel Named Billy, An', 'http://dummyimage.com/166x140.jpg/dddddd/000000', 'single'),
	('Barkleys of Broadway, The', 'http://dummyimage.com/178x175.jpg/cc0000/ffffff', 'EP'),
	('Alive Inside', 'http://dummyimage.com/105x148.png/5fa2dd/ffffff', 'EP'),
	('Hidden Agenda', 'http://dummyimage.com/209x114.jpg/cc0000/ffffff', 'single'),
	('Bleak Moments', 'http://dummyimage.com/231x140.bmp/5fa2dd/ffffff', 'EP'),
	('¡Alambrista! (Illegal, The)', 'http://dummyimage.com/154x182.bmp/cc0000/ffffff', 'EP'),
	('Charlie Chan in Rio', 'http://dummyimage.com/160x247.png/ff4444/ffffff', 'EP'),
	('Satan''s Little Helper', 'http://dummyimage.com/186x189.png/cc0000/ffffff', 'single'),
	('Ladykillers, The', 'http://dummyimage.com/108x208.png/dddddd/000000', 'EP'),
	('Tremors II: Aftershocks', 'http://dummyimage.com/223x241.bmp/ff4444/ffffff', 'album'),
	('Master, The (Huang Fei Hong jiu er zhi long xing tian xia)', 'http://dummyimage.com/158x143.jpg/ff4444/ffffff', 'album'),
	('Reservoir Dogs', 'http://dummyimage.com/148x161.png/cc0000/ffffff', 'EP'),
	('Adam''s Apples (Adams æbler)', 'http://dummyimage.com/109x114.jpg/dddddd/000000', 'single'),
	('Water', 'http://dummyimage.com/178x165.bmp/5fa2dd/ffffff', 'EP'),
	('The Harmony Game', 'http://dummyimage.com/175x229.png/cc0000/ffffff', 'EP'),
	('Rosa Luxemburg', 'http://dummyimage.com/205x219.bmp/dddddd/000000', 'single'),
	('Battle of Algiers, The (La battaglia di Algeri)', 'http://dummyimage.com/149x111.png/dddddd/000000', 'album'),
	('Fearful Symmetry: The Making of ''To Kill a Mockingbird''', 'http://dummyimage.com/151x173.png/ff4444/ffffff', 'album'),
	('Journey for Margaret', 'http://dummyimage.com/146x122.jpg/cc0000/ffffff', 'EP'),
	('Kestrel''s Eye (Falkens öga)', 'http://dummyimage.com/236x210.jpg/dddddd/000000', 'single'),
	('Vince Vaughn''s Wild West Comedy Show: 30 Days & 30 Nights - Hollywood to the Heartland', 'http://dummyimage.com/137x200.jpg/ff4444/ffffff', 'EP'),
	('Them (Ils)', 'http://dummyimage.com/120x148.png/5fa2dd/ffffff', 'single'),
	('Middle of Nowhere', 'http://dummyimage.com/120x221.bmp/5fa2dd/ffffff', 'EP'),
	('Planet of Dinosaurs', 'http://dummyimage.com/106x208.jpg/5fa2dd/ffffff', 'EP'),
	('Pillow Book, The', 'http://dummyimage.com/154x198.bmp/dddddd/000000', 'EP'),
	('Nothing Like the Holidays', 'http://dummyimage.com/201x231.bmp/5fa2dd/ffffff', 'album'),
	('The Divine Woman', 'http://dummyimage.com/224x146.jpg/ff4444/ffffff', 'single'),
	('Super Demetrios', 'http://dummyimage.com/167x120.jpg/5fa2dd/ffffff', 'single'),
	('Baby Geniuses', 'http://dummyimage.com/181x171.jpg/5fa2dd/ffffff', 'single'),
	('Transylmania', 'http://dummyimage.com/120x105.jpg/dddddd/000000', 'single'),
	('Tale of Winter, A (a.k.a. A Winter''s Tale) (Conte d''hiver)', 'http://dummyimage.com/131x130.png/cc0000/ffffff', 'album'),
	('Bitter Victory', 'http://dummyimage.com/225x228.jpg/cc0000/ffffff', 'album'),
	('Green Ice', 'http://dummyimage.com/132x136.bmp/dddddd/000000', 'album'),
	('Middle of the World, The (O Caminho das Nuvens)', 'http://dummyimage.com/156x138.bmp/ff4444/ffffff', 'album'),
	('Buffalo Girls', 'http://dummyimage.com/109x121.jpg/cc0000/ffffff', 'single'),
	('Bloody New Year', 'http://dummyimage.com/206x161.bmp/cc0000/ffffff', 'album'),
	('Soldier''s Story, A', 'http://dummyimage.com/175x120.bmp/cc0000/ffffff', 'EP'),
	('5 Dolls for an August Moon (5 bambole per la luna d''agosto)', 'http://dummyimage.com/225x125.jpg/ff4444/ffffff', 'album'),
	('Street Fight', 'http://dummyimage.com/134x124.jpg/cc0000/ffffff', 'single'),
	('Firecracker', 'http://dummyimage.com/166x162.bmp/cc0000/ffffff', 'EP'),
	('We''re the Millers', 'http://dummyimage.com/140x207.jpg/dddddd/000000', 'album'),
	('Boats', 'http://dummyimage.com/199x200.jpg/dddddd/000000', 'single'),
	('Chapter 27', 'http://dummyimage.com/128x124.png/cc0000/ffffff', 'EP'),
	('Into the Storm', 'http://dummyimage.com/245x152.bmp/5fa2dd/ffffff', 'single'),
	('Only When I Laugh', 'http://dummyimage.com/170x156.jpg/cc0000/ffffff', 'single'),
	('Quest, The', 'http://dummyimage.com/225x234.png/ff4444/ffffff', 'album'),
	('Without Pity', 'http://dummyimage.com/174x161.bmp/5fa2dd/ffffff', 'single'),
	('Northanger Abbey', 'http://dummyimage.com/206x241.jpg/5fa2dd/ffffff', 'EP'),
	('Chicago Joe and the Showgirl', 'http://dummyimage.com/222x232.png/ff4444/ffffff', 'album'),
	('Haunted Palace, The', 'http://dummyimage.com/143x230.bmp/dddddd/000000', 'EP'),
	('Casual Relations', 'http://dummyimage.com/245x223.jpg/5fa2dd/ffffff', 'album'),
	('Little Nicky', 'http://dummyimage.com/170x118.jpg/dddddd/000000', 'EP'),
	('Made of Honor', 'http://dummyimage.com/101x248.bmp/cc0000/ffffff', 'album'),
	('Apollo 13', 'http://dummyimage.com/239x133.png/ff4444/ffffff', 'EP'),
	('Caine (Shark!)', 'http://dummyimage.com/144x128.png/dddddd/000000', 'single'),
	('The First Movie', 'http://dummyimage.com/185x144.bmp/cc0000/ffffff', 'EP'),
	('Brooklyn', 'http://dummyimage.com/121x250.bmp/ff4444/ffffff', 'album'),
	('Direct from Brooklyn', 'http://dummyimage.com/104x169.jpg/ff4444/ffffff', 'album'),
	('Immortals', 'http://dummyimage.com/213x102.png/5fa2dd/ffffff', 'EP'),
	('Light Years Away', 'http://dummyimage.com/139x132.jpg/dddddd/000000', 'single'),
	('Intentions of Murder (a.k.a. Murderous Instincts) (Akai satsui)', 'http://dummyimage.com/150x231.png/cc0000/ffffff', 'album'),
	('Sixtynine', 'http://dummyimage.com/137x160.bmp/ff4444/ffffff', 'album'),
	('Prelude to War (Why We Fight, 1)', 'http://dummyimage.com/196x131.png/cc0000/ffffff', 'single'),
	('Arrested Development Documentary Project, The', 'http://dummyimage.com/192x238.png/ff4444/ffffff', 'single'),
	('Possession of Joel Delaney, The', 'http://dummyimage.com/175x241.bmp/dddddd/000000', 'EP'),
	('Point Blank', 'http://dummyimage.com/128x228.png/5fa2dd/ffffff', 'album'),
	('Speed', 'http://dummyimage.com/189x233.png/cc0000/ffffff', 'EP'),
	('Damage (Fatale)', 'http://dummyimage.com/212x188.bmp/5fa2dd/ffffff', 'single'),
	('Very Happy Alexander (Alexandre le bienheureux)', 'http://dummyimage.com/113x129.bmp/dddddd/000000', 'single'),
	('Meet Monica Velour', 'http://dummyimage.com/158x136.png/cc0000/ffffff', 'album'),
	('Due Date', 'http://dummyimage.com/156x118.bmp/ff4444/ffffff', 'album'),
	('Don''t Move (Non ti muovere)', 'http://dummyimage.com/180x138.jpg/ff4444/ffffff', 'single'),
	('Over Your Cities Grass Will Grow', 'http://dummyimage.com/216x197.png/ff4444/ffffff', 'album'),
	('List of Adrian Messenger, The', 'http://dummyimage.com/176x170.bmp/ff4444/ffffff', 'album'),
	('Saved!', 'http://dummyimage.com/222x107.png/cc0000/ffffff', 'album'),
	('Tales from the Darkside: The Movie', 'http://dummyimage.com/214x130.bmp/cc0000/ffffff', 'single'),
	('Swimsuit Issue, The (Allt flyter)', 'http://dummyimage.com/145x237.png/cc0000/ffffff', 'EP'),
	('Adventures of Sebastian Cole, The', 'http://dummyimage.com/170x220.png/cc0000/ffffff', 'album'),
	('Curse of the Golden Flower (Man cheng jin dai huang jin jia)', 'http://dummyimage.com/141x126.png/dddddd/000000', 'EP'),
	('Fresh Horses', 'http://dummyimage.com/204x209.jpg/5fa2dd/ffffff', 'album'),
	('Saddest Music in the World, The', 'http://dummyimage.com/225x239.png/cc0000/ffffff', 'EP'),
	('Contagion / Bio Slime', 'http://dummyimage.com/174x228.png/5fa2dd/ffffff', 'single'),
	('Grande école', 'http://dummyimage.com/154x203.jpg/dddddd/000000', 'EP'),
	('Of Horses and Men', 'http://dummyimage.com/226x169.jpg/dddddd/000000', 'single'),
	('Tiny Toon Adventures: How I Spent My Vacation', 'http://dummyimage.com/124x181.bmp/dddddd/000000', 'single'),
	('The Power and the Glory', 'http://dummyimage.com/249x214.jpg/5fa2dd/ffffff', 'album'),
	('Lemonade Joe (Limonádový Joe aneb Konská opera)', 'http://dummyimage.com/181x173.bmp/ff4444/ffffff', 'EP'),
	('The Police Can''t Move', 'http://dummyimage.com/195x176.png/ff4444/ffffff', 'single'),
	('Swoon', 'http://dummyimage.com/106x183.jpg/cc0000/ffffff', 'album'),
	('Muppet Family Christmas, A', 'http://dummyimage.com/242x191.bmp/dddddd/000000', 'EP'),
	('Blown Away', 'http://dummyimage.com/107x108.bmp/cc0000/ffffff', 'EP'),
	('Bats', 'http://dummyimage.com/125x229.bmp/ff4444/ffffff', 'album'),
	('Killing, The', 'http://dummyimage.com/123x215.bmp/5fa2dd/ffffff', 'album'),
	('Back to the USSR - takaisin Ryssiin', 'http://dummyimage.com/237x201.bmp/ff4444/ffffff', 'album'),
	('Merry Madagascar', 'http://dummyimage.com/180x233.bmp/5fa2dd/ffffff', 'EP'),
	('International House', 'http://dummyimage.com/153x187.bmp/dddddd/000000', 'EP'),
	('Ugly American, The', 'http://dummyimage.com/188x245.bmp/dddddd/000000', 'album'),
	('The Third Reich: The Rise & Fall', 'http://dummyimage.com/151x107.jpg/ff4444/ffffff', 'album'),
	('Family Guy Presents Stewie Griffin: The Untold Story', 'http://dummyimage.com/207x210.bmp/dddddd/000000', 'EP'),
	('He Got Game', 'http://dummyimage.com/250x133.jpg/cc0000/ffffff', 'album'),
	('Sun Kissed', 'http://dummyimage.com/118x111.jpg/ff4444/ffffff', 'EP'),
	('Bay of Angels (La baie des anges)', 'http://dummyimage.com/198x202.bmp/dddddd/000000', 'EP'),
	('Seasoning House, The', 'http://dummyimage.com/196x212.jpg/ff4444/ffffff', 'album'),
	('Circles (Krugovi)', 'http://dummyimage.com/231x197.bmp/cc0000/ffffff', 'EP'),
	('Spider', 'http://dummyimage.com/122x179.jpg/dddddd/000000', 'EP'),
	('Man Who Wasn''t There, The', 'http://dummyimage.com/119x184.bmp/ff4444/ffffff', 'EP'),
	('Paper Lion', 'http://dummyimage.com/189x230.bmp/cc0000/ffffff', 'single'),
	('Stranger, The (Straniero, Lo)', 'http://dummyimage.com/115x112.bmp/5fa2dd/ffffff', 'EP'),
	('Romance in Manhattan', 'http://dummyimage.com/181x189.jpg/cc0000/ffffff', 'EP'),
	('Tokyo Olympiad', 'http://dummyimage.com/195x125.bmp/ff4444/ffffff', 'EP'),
	('Babysitting', 'http://dummyimage.com/115x237.png/ff4444/ffffff', 'EP'),
	('S. Darko (S. Darko: A Donnie Darko Tale)', 'http://dummyimage.com/218x199.jpg/cc0000/ffffff', 'EP'),
	('Wackness, The', 'http://dummyimage.com/121x170.jpg/cc0000/ffffff', 'single'),
	('Alias the Doctor', 'http://dummyimage.com/109x158.jpg/dddddd/000000', 'album'),
	('Io Island (Iodo)', 'http://dummyimage.com/152x207.jpg/ff4444/ffffff', 'album'),
	('After the Rain (Ame agaru) ', 'http://dummyimage.com/158x144.bmp/ff4444/ffffff', 'album'),
	('Food of the Gods, The', 'http://dummyimage.com/238x219.png/cc0000/ffffff', 'album'),
	('Cypher', 'http://dummyimage.com/219x105.jpg/dddddd/000000', 'album'),
	('About Cherry', 'http://dummyimage.com/211x214.jpg/ff4444/ffffff', 'EP'),
	('Nightmare on Elm Street, A', 'http://dummyimage.com/163x206.jpg/5fa2dd/ffffff', 'EP'),
	('Man Who Laughs, The', 'http://dummyimage.com/201x190.png/5fa2dd/ffffff', 'single'),
	('Shock Treatment', 'http://dummyimage.com/248x110.bmp/5fa2dd/ffffff', 'EP'),
	('Artemisia', 'http://dummyimage.com/190x240.bmp/5fa2dd/ffffff', 'EP'),
	('Harold and Maude', 'http://dummyimage.com/243x173.bmp/5fa2dd/ffffff', 'single'),
	('Marine, The', 'http://dummyimage.com/118x151.png/ff4444/ffffff', 'EP'),
	('Wasp Woman, The', 'http://dummyimage.com/123x179.bmp/5fa2dd/ffffff', 'album'),
	('Winged Creatures (Fragments)', 'http://dummyimage.com/204x185.jpg/5fa2dd/ffffff', 'EP'),
	('Shadow Dancer, The (Shadows in the Sun)', 'http://dummyimage.com/237x188.jpg/ff4444/ffffff', 'EP'),
	('Vincent', 'http://dummyimage.com/119x177.jpg/5fa2dd/ffffff', 'album'),
	('Nights in Rodanthe', 'http://dummyimage.com/221x176.png/ff4444/ffffff', 'album'),
	('Run If You Can', 'http://dummyimage.com/179x156.jpg/ff4444/ffffff', 'EP'),
	('Kite Runner, The', 'http://dummyimage.com/181x102.bmp/dddddd/000000', 'album'),
	('Mystery (Fu cheng mi shi)', 'http://dummyimage.com/118x233.png/dddddd/000000', 'album'),
	('Thief of Bagdad, The', 'http://dummyimage.com/162x207.png/dddddd/000000', 'album'),
	('Where the Buffalo Roam', 'http://dummyimage.com/218x118.bmp/5fa2dd/ffffff', 'EP'),
	('Children of the Corn III', 'http://dummyimage.com/110x149.bmp/ff4444/ffffff', 'EP'),
	('High Plains Drifter', 'http://dummyimage.com/165x221.png/dddddd/000000', 'single'),
	('Final Destination 5', 'http://dummyimage.com/208x183.png/cc0000/ffffff', 'EP'),
	('Chorus, The (Choristes, Les)', 'http://dummyimage.com/250x212.bmp/5fa2dd/ffffff', 'EP'),
	('I Know What I Saw', 'http://dummyimage.com/117x138.jpg/5fa2dd/ffffff', 'album'),
	('Jason Goes to Hell: The Final Friday', 'http://dummyimage.com/161x183.jpg/dddddd/000000', 'EP'),
	('Love Me Tonight', 'http://dummyimage.com/211x170.jpg/cc0000/ffffff', 'EP'),
	('Wadd: The Life & Times of John C. Holmes', 'http://dummyimage.com/181x227.png/dddddd/000000', 'single'),
	('Two Women', 'http://dummyimage.com/131x139.bmp/dddddd/000000', 'EP'),
	('Ten Inch Hero', 'http://dummyimage.com/197x162.bmp/dddddd/000000', 'EP'),
	('Ikigami', 'http://dummyimage.com/143x129.png/5fa2dd/ffffff', 'album'),
	('Safe Passage', 'http://dummyimage.com/187x101.jpg/ff4444/ffffff', 'single'),
	('Dark Girls', 'http://dummyimage.com/123x224.png/5fa2dd/ffffff', 'EP'),
	('Penitentiary II', 'http://dummyimage.com/176x118.bmp/dddddd/000000', 'album'),
	('Blue Gold: World Water Wars', 'http://dummyimage.com/187x211.jpg/dddddd/000000', 'EP'),
	('Peacemaker, The', 'http://dummyimage.com/221x156.bmp/ff4444/ffffff', 'album'),
	('Clockmaker of St. Paul, The (L''horloger de Saint-Paul)', 'http://dummyimage.com/203x241.bmp/dddddd/000000', 'EP'),
	('Tyler Perry''s Meet the Browns', 'http://dummyimage.com/180x164.png/5fa2dd/ffffff', 'single'),
	('Guy X', 'http://dummyimage.com/102x216.png/ff4444/ffffff', 'single'),
	('Lotta 2: Lotta flyttar hemifrån', 'http://dummyimage.com/153x155.jpg/dddddd/000000', 'EP'),
	('Grudge 2, The', 'http://dummyimage.com/164x203.bmp/ff4444/ffffff', 'EP'),
	('Opportunity Knocks', 'http://dummyimage.com/121x167.png/cc0000/ffffff', 'single'),
	('Love Serenade', 'http://dummyimage.com/180x121.jpg/5fa2dd/ffffff', 'single'),
	('Grindhouse', 'http://dummyimage.com/130x173.jpg/5fa2dd/ffffff', 'EP'),
	('One for the Money', 'http://dummyimage.com/150x173.bmp/cc0000/ffffff', 'EP'),
	('Beloved', 'http://dummyimage.com/113x117.png/5fa2dd/ffffff', 'single'),
	('Reach the Rock', 'http://dummyimage.com/163x141.png/ff4444/ffffff', 'EP'),
	('Mom and Dad Save the World', 'http://dummyimage.com/229x196.png/dddddd/000000', 'album'),
	('Spend It All', 'http://dummyimage.com/195x128.bmp/ff4444/ffffff', 'single'),
	('Jönssonligan spelar högt', 'http://dummyimage.com/157x101.jpg/dddddd/000000', 'single'),
	('Wild, The', 'http://dummyimage.com/142x144.jpg/ff4444/ffffff', 'album'),
	('And the Band Played On', 'http://dummyimage.com/173x151.png/cc0000/ffffff', 'EP'),
	('Amu', 'http://dummyimage.com/145x152.bmp/5fa2dd/ffffff', 'EP'),
	('Mattei Affair, The (Il caso Mattei)', 'http://dummyimage.com/128x159.jpg/cc0000/ffffff', 'EP'),
	('Picnic on the Grass (Le déjeuner sur l''herbe)', 'http://dummyimage.com/110x155.jpg/5fa2dd/ffffff', 'EP'),
	('13Hrs', 'http://dummyimage.com/219x177.bmp/ff4444/ffffff', 'EP'),
	('Police Academy 6: City Under Siege', 'http://dummyimage.com/233x239.png/ff4444/ffffff', 'EP'),
	('Terminator Salvation', 'http://dummyimage.com/211x209.png/ff4444/ffffff', 'single'),
	('Humble Pie (American Fork)', 'http://dummyimage.com/228x200.jpg/dddddd/000000', 'single'),
	('Hellsinki (Rööperi)', 'http://dummyimage.com/144x157.png/ff4444/ffffff', 'single'),
	('Dead Snow (Død snø)', 'http://dummyimage.com/141x205.bmp/5fa2dd/ffffff', 'single'),
	('Somebody Up There Likes Me', 'http://dummyimage.com/145x127.bmp/ff4444/ffffff', 'album'),
	('Shadowlands', 'http://dummyimage.com/128x239.png/ff4444/ffffff', 'single'),
	('Sun, The (Solntse)', 'http://dummyimage.com/180x236.png/5fa2dd/ffffff', 'EP'),
	('All Superheros Must Die', 'http://dummyimage.com/173x114.png/dddddd/000000', 'album'),
	('Fast & Furious 6 (Fast and the Furious 6, The)', 'http://dummyimage.com/242x161.bmp/ff4444/ffffff', 'album'),
	('Turtles Can Fly (Lakposhtha hâm parvaz mikonand)', 'http://dummyimage.com/209x121.bmp/ff4444/ffffff', 'single'),
	('Song of Freedom', 'http://dummyimage.com/170x152.bmp/dddddd/000000', 'album'),
	('Waiting...', 'http://dummyimage.com/147x117.png/ff4444/ffffff', 'album'),
	('Ward 13', 'http://dummyimage.com/238x234.bmp/cc0000/ffffff', 'single'),
	('Hanna', 'http://dummyimage.com/165x114.jpg/ff4444/ffffff', 'EP'),
	('Time to Live, a Time to Die, A (Tong nien wang shi)', 'http://dummyimage.com/210x120.png/ff4444/ffffff', 'single'),
	('Jack the Giant Slayer', 'http://dummyimage.com/212x229.bmp/ff4444/ffffff', 'album'),
	('An Empress and the Warriors', 'http://dummyimage.com/117x156.jpg/ff4444/ffffff', 'single'),
	('Blind Sunflowers, The (Los girasoles ciegos)', 'http://dummyimage.com/186x216.jpg/dddddd/000000', 'EP'),
	('Family Resemblances (Un air de famille)', 'http://dummyimage.com/238x169.png/dddddd/000000', 'EP'),
	('All About Eve', 'http://dummyimage.com/107x119.png/ff4444/ffffff', 'single'),
	('Stanley Kubrick''s Boxes', 'http://dummyimage.com/191x130.bmp/dddddd/000000', 'single'),
	('Wetherby', 'http://dummyimage.com/103x128.bmp/cc0000/ffffff', 'single'),
	('Low Life, The', 'http://dummyimage.com/104x204.bmp/5fa2dd/ffffff', 'album'),
	('Kicking & Screaming', 'http://dummyimage.com/101x222.jpg/cc0000/ffffff', 'EP'),
	('Betty', 'http://dummyimage.com/118x140.jpg/ff4444/ffffff', 'single'),
	('Conceiving Ada', 'http://dummyimage.com/213x171.png/5fa2dd/ffffff', 'single'),
	('Hannah and Her Sisters', 'http://dummyimage.com/197x186.jpg/5fa2dd/ffffff', 'EP'),
	('Benny''s Video', 'http://dummyimage.com/188x181.bmp/ff4444/ffffff', 'album'),
	('Phantom Lover, The (Ye ban ge sheng)', 'http://dummyimage.com/238x154.jpg/5fa2dd/ffffff', 'EP'),
	('Moonraker', 'http://dummyimage.com/149x214.png/5fa2dd/ffffff', 'album'),
	('I''ll Be Seeing You', 'http://dummyimage.com/191x214.jpg/cc0000/ffffff', 'single'),
	('Smart Money', 'http://dummyimage.com/215x129.png/ff4444/ffffff', 'EP'),
	('Doctor Takes a Wife, The', 'http://dummyimage.com/246x239.jpg/ff4444/ffffff', 'EP'),
	('Coming Out', 'http://dummyimage.com/142x214.jpg/dddddd/000000', 'single'),
	('Country', 'http://dummyimage.com/190x166.bmp/dddddd/000000', 'EP'),
	('One of Our Aircraft Is Missing', 'http://dummyimage.com/153x197.bmp/cc0000/ffffff', 'single'),
	('Rocky Horror Picture Show, The', 'http://dummyimage.com/240x134.png/5fa2dd/ffffff', 'album'),
	('My Friends (Amici miei)', 'http://dummyimage.com/155x219.png/5fa2dd/ffffff', 'album'),
	('Black Like Me', 'http://dummyimage.com/195x108.bmp/ff4444/ffffff', 'album'),
	('Fork in the Road, A', 'http://dummyimage.com/121x144.bmp/ff4444/ffffff', 'EP'),
	('Working Class Goes to Heaven, The (a.k.a. Lulu the Tool) (La classe operaia va in paradiso)', 'http://dummyimage.com/210x174.png/ff4444/ffffff', 'single'),
	('Profession of Arms, The (Il mestiere delle armi)', 'http://dummyimage.com/192x131.jpg/cc0000/ffffff', 'EP'),
	('Underworld', 'http://dummyimage.com/151x191.jpg/cc0000/ffffff', 'album'),
	('What Fault Is It of Ours?', 'http://dummyimage.com/113x126.jpg/dddddd/000000', 'album'),
	('Snake and Mongoose', 'http://dummyimage.com/230x225.png/5fa2dd/ffffff', 'single'),
	('The Last Time I Saw Macao', 'http://dummyimage.com/234x114.bmp/cc0000/ffffff', 'EP'),
	('Urban Legends: Bloody Mary', 'http://dummyimage.com/218x196.jpg/ff4444/ffffff', 'single'),
	('Bad Chicken', 'http://dummyimage.com/125x163.jpg/dddddd/000000', 'EP'),
	('L''Italien', 'http://dummyimage.com/149x203.png/5fa2dd/ffffff', 'single'),
	('True Confession', 'http://dummyimage.com/148x117.jpg/cc0000/ffffff', 'EP'),
	('Once Upon a Time in Anatolia (Bir zamanlar Anadolu''da)', 'http://dummyimage.com/103x137.bmp/ff4444/ffffff', 'single'),
	('Defender, The', 'http://dummyimage.com/175x104.jpg/dddddd/000000', 'EP'),
	('Bad Family (Paha Perhe)', 'http://dummyimage.com/128x237.png/dddddd/000000', 'album'),
	('Shanks', 'http://dummyimage.com/199x122.bmp/ff4444/ffffff', 'album'),
	('Volga - Volga', 'http://dummyimage.com/234x156.jpg/dddddd/000000', 'album'),
	('Now You Know', 'http://dummyimage.com/233x165.jpg/ff4444/ffffff', 'single'),
	('Lord of War', 'http://dummyimage.com/230x191.bmp/ff4444/ffffff', 'album'),
	('Wild Thornberrys Movie, The', 'http://dummyimage.com/200x153.bmp/ff4444/ffffff', 'single'),
	('Supercross', 'http://dummyimage.com/137x199.bmp/dddddd/000000', 'album'),
	('Farah Goes Bang', 'http://dummyimage.com/115x227.jpg/dddddd/000000', 'album'),
	('Exterminator, The', 'http://dummyimage.com/162x136.jpg/dddddd/000000', 'EP'),
	('Capitalism: A Love Story', 'http://dummyimage.com/202x115.bmp/dddddd/000000', 'album'),
	('How High', 'http://dummyimage.com/140x183.jpg/cc0000/ffffff', 'album'),
	('Peter Pan', 'http://dummyimage.com/134x191.png/ff4444/ffffff', 'single'),
	('London After Midnight', 'http://dummyimage.com/220x126.bmp/ff4444/ffffff', 'EP'),
	('Dr. T and the Women', 'http://dummyimage.com/115x137.bmp/cc0000/ffffff', 'album'),
	('13 Going on 30', 'http://dummyimage.com/119x206.bmp/ff4444/ffffff', 'EP'),
	('Farewell, The (Abschied - Brechts letzter Sommer)', 'http://dummyimage.com/188x235.jpg/5fa2dd/ffffff', 'album'),
	('Fathom', 'http://dummyimage.com/205x235.jpg/dddddd/000000', 'EP'),
	('Blame It on Rio', 'http://dummyimage.com/105x114.jpg/cc0000/ffffff', 'single'),
	('Daughter of Dr. Jeckyll', 'http://dummyimage.com/108x116.bmp/5fa2dd/ffffff', 'album'),
	('Oliver Twist', 'http://dummyimage.com/101x243.png/dddddd/000000', 'single'),
	('Ollin oppivuodet', 'http://dummyimage.com/200x230.jpg/5fa2dd/ffffff', 'single'),
	('Support Your Local Gunfighter', 'http://dummyimage.com/235x110.bmp/ff4444/ffffff', 'EP'),
	('Atlantis: The Lost Empire', 'http://dummyimage.com/121x194.bmp/ff4444/ffffff', 'album'),
	('8 (8, the Play)', 'http://dummyimage.com/122x138.bmp/cc0000/ffffff', 'EP'),
	('Hedwig and the Angry Inch', 'http://dummyimage.com/232x102.png/ff4444/ffffff', 'EP'),
	('Roll Bounce', 'http://dummyimage.com/216x130.bmp/cc0000/ffffff', 'single'),
	('Pain in the Ass, A (L''emmerdeur)', 'http://dummyimage.com/131x243.jpg/5fa2dd/ffffff', 'EP'),
	('Idolmaker, The', 'http://dummyimage.com/196x236.png/ff4444/ffffff', 'EP'),
	('Dragon Ball Z the Movie: The Tree of Might (Doragon bôru Z 3: Chikyû marugoto chô kessen)', 'http://dummyimage.com/248x226.png/5fa2dd/ffffff', 'single'),
	('Jour se lève, Le (Daybreak)', 'http://dummyimage.com/135x137.bmp/ff4444/ffffff', 'single'),
	('Quinceañera', 'http://dummyimage.com/150x216.png/cc0000/ffffff', 'EP'),
	('Seventh Son', 'http://dummyimage.com/149x114.png/5fa2dd/ffffff', 'EP'),
	('God Save the King', 'http://dummyimage.com/207x219.png/dddddd/000000', 'album'),
	('Red''s Dream', 'http://dummyimage.com/133x170.jpg/cc0000/ffffff', 'single'),
	('Tasting Menu', 'http://dummyimage.com/142x124.bmp/cc0000/ffffff', 'single'),
	('Babysitter, The', 'http://dummyimage.com/161x219.bmp/ff4444/ffffff', 'EP'),
	('Black Cloud', 'http://dummyimage.com/189x186.jpg/ff4444/ffffff', 'single'),
	('Threesome', 'http://dummyimage.com/143x118.bmp/dddddd/000000', 'EP'),
	('Less is More (Menos es más)', 'http://dummyimage.com/113x190.jpg/cc0000/ffffff', 'EP'),
	('Crazy on the Outside', 'http://dummyimage.com/148x241.png/5fa2dd/ffffff', 'EP'),
	('Mr. Wu', 'http://dummyimage.com/246x235.png/5fa2dd/ffffff', 'single'),
	('Gate of Flesh (Nikutai no mon)', 'http://dummyimage.com/179x249.bmp/ff4444/ffffff', 'album'),
	('Looking for Maria Sanchez', 'http://dummyimage.com/113x220.bmp/ff4444/ffffff', 'single'),
	('Gulliver''s Travels', 'http://dummyimage.com/247x145.bmp/dddddd/000000', 'EP'),
	('Hunt for Red October, The', 'http://dummyimage.com/230x234.bmp/dddddd/000000', 'single'),
	('Male Domination', 'http://dummyimage.com/249x243.bmp/5fa2dd/ffffff', 'single'),
	('Seyyit Khan: Bride of the Earth (Seyyit Han)', 'http://dummyimage.com/207x213.jpg/dddddd/000000', 'EP'),
	('Mrs. Parkington', 'http://dummyimage.com/119x203.png/cc0000/ffffff', 'EP'),
	('Blown Away', 'http://dummyimage.com/243x197.bmp/5fa2dd/ffffff', 'EP'),
	('Blue Sky', 'http://dummyimage.com/198x129.png/dddddd/000000', 'EP'),
	('Confession, The (L''aveu)', 'http://dummyimage.com/192x101.png/dddddd/000000', 'EP'),
	('Christmas Memory, A (Truman Capote''s ''A Christmas Memory'')', 'http://dummyimage.com/203x242.jpg/cc0000/ffffff', 'album'),
	('Chinese Zodiac (Armour of God III) (CZ12)', 'http://dummyimage.com/183x152.png/cc0000/ffffff', 'EP'),
	('Dragon Ball Z: The Return of Cooler (Doragon bôru Z 6: Gekitotsu! Hyakuoku pawâ no senshi)', 'http://dummyimage.com/184x126.bmp/cc0000/ffffff', 'album'),
	('Doghouse', 'http://dummyimage.com/164x166.png/cc0000/ffffff', 'EP'),
	('First Strike (Police Story 4: First Strike) (Ging chaat goo si 4: Ji gaan daan yam mo)', 'http://dummyimage.com/167x247.jpg/ff4444/ffffff', 'EP'),
	('Men Who Tread on the Tiger''s Tail, The (Tora no o wo fumu otokotachi)', 'http://dummyimage.com/163x250.jpg/cc0000/ffffff', 'album'),
	('Tell No One (Ne le dis à personne)', 'http://dummyimage.com/227x242.jpg/ff4444/ffffff', 'single');

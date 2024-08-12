import os
os.chdir(os.path.abspath(os.path.dirname(__file__)))
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)


class Label:
	def __init__(self:object, menu:str, preOffset:int = -1, offset:int = 0, encoding:str = "utf-8") -> object:
		self.__menu = str(menu)
		try:
			self.__preOffset = int(preOffset)
		except:
			print("The value of the preOffset is invalid. It is defaulted to -1. ")
			self.__preOffset = -1
		try:
			self.__offset = int(offset)
		except:
			print("The value of the offset is invalid. It is defaulted to 0. ")
			self.__offset = 0
		self.__encoding = str(encoding)
		self.__labels = []
	def __romanToInt(self:object, value:str) -> int:
		a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
		s = str(value)
		ans = 0
		try:
			for i in range(len(s)):
				if i < len(s)-1 and a[s[i]] < a[s[i+1]]:
					ans -= a[s[i]]
				else:
					ans += a[s[i]]
			return ans
		except:
			return None
	def resolve(self:object) -> int:
		self.__labels.clear()
		for line in self.__menu.split("\n"):
			if "…" in line:
				keyValue = line.split("…")
				key = keyValue[0]
				value = keyValue[-1]
				try:
					value = int(value)
					flag = True # add offset
				except:
					value = self.__romanToInt(value)
					flag = False # do not add offset
				if value is not None:
					self.__labels.append((key, value + self.__offset if flag else value + self.__preOffset))
		print("Labels generated are as follows. \n{0}".format(self.__labels))
		return len(self.__labels)
	def generate(self:object, xmlFp:str) -> bool:
		if isinstance(xmlFp, str):
			xmlPath = xmlFp.replace("\"", "")
			try:
				if os.path.isfile(xmlPath):
					os.system("attrib -a -h -r -s \"{0}\"".format(xmlPath))
				with open(xmlPath, "w", encoding = self.__encoding) as f:
					f.write(str(self))
				print("Successfully write to \"{0}\". ".format(xmlPath))
				os.system("attrib +a -h +r +s \"{0}\"".format(__file__))
				os.system("attrib +a -h +r +s \"{0}\"".format(xmlPath))
				return True
			except Exception as e:
				print("Failed to write to \"{0}\". Details are as follows. \n{1}".format(xmlPath, e))
				return False
		else:
			print(self)
	def __str__(self:object) -> str:
		sRet = "<?xml version=\"1.0\" encoding=\"{0}\"?>\n<BOOKMARKS>\n\t<INFO PRODUCER=\"WPS PDF\"/>\n".format(self.__encoding)
		for label in self.__labels:
			sRet += "\t<ITEM INDENT=\"1\" OPEN=\"1\" FONTSTYLE=\"0\" COLOR=\"4278190080\" ZOOMMODE=\"0\" PARMA=\"0.000000,0.000000,0.000000,0.000000\" PAGE=\"{1}\" NAME=\"{0}\"/>\n".format(label[0], label[1])
		sRet += "</BOOKMARKS>"
		return sRet


def main() -> int:
	menu = "绪言………………………………………………………………………………………………I\n钢琴音调特征……………………………………………………………………………………II\n演奏参数或说明（仅供参考）……………………………………………………………………IV\n《4分33秒》演奏方法…………………………………………………………………………IV\n01．星空……………………………………… ……………………………………………………1\n02．Still Water……………………………………………………………………………………9\n03．亲亲宝贝……………………………………………………………………………………15\n04．Santorini…………………………………………………………………………………20\n05．小小竹排……………………………………………………………………………………41\n06．Etude in B Major……………………………………………………………………………41\n07．Air For The G String…………………………………………………………………………50\n08．New Morning……………………………………………………………………… ………52\n09．心兰相随……………………………………………………………………………………54\n10．圣托里尼……………………………………………………………………………………63\n11．梦中的婚礼…………………………………………………………………………………78\n12．瓦妮莎的微笑………………………………………………………………………………80\n13．水边的阿狄丽娜……………………………………………………………………………89\n14．梦中的鸟……………………………………………………………………………………89\n15．给母亲的信…………………………………………………………………………………94\n16．Felitsa……………………… ………………………………………………………………98\n17．Victory Remix………………………………………………………………… ……………106\n18．The Storm…………………………………………………………………………………118\n19．Vertigo………………………………………………………………………………………154\n20．Into the Deep Blue…………………………………………………… ……………………156\n21．Dance for Me………………………………………………………………………………139\n22．Renegade…………………………………………………………………………………144\n23．Keys to Imagination………………………………………………………………………155\n24．加勒比海盗…………………………………………………………………………………165\n25．爱的协奏曲…………………………………………………………………………………201\n26．Desire………………………………………………………… …………………………206\n27．The End of August………………………………………………………………………209\n28．月光奏鸣曲 …………………………………………………………………………………193\n29．Until the Last Moment…………………………………………………………………214\n30．夜莺…………………………………………………………………………………………220\n31．Truth of Touch…………………………………………………………………………231\n32．Reflections of Passion………………………………… ………………………………237\n33．Swept Away……………………………………………………………………………242\n34．Waltz in 7/8………………………………………………………………………………247\n35．Adagio in C Minor………………………………………………………………………255\n36．Standing in Motion……………………………………………………………………259\n37．Aria………………………………………………………………………………………264\n38．幽默曲………………………………………………………… ……………………………266\n39．D大调小步舞曲……………………………………………………………………………270\n40．Kiki's Delivery Service……………………………………………………………………272\n41．永远同在……………………………………………… ……………………………………281\n42．夜的钢琴曲五………………………………………………………………………………285\n43．匈牙利奏鸣曲………………………………………………………………………………294\n44．渴望……………………………………………… …………………………………………294\n45．A Love for Life……………………………………………………………………………300\n46．If I Could Tell You…………………………………………………………………………308\n47．Enchantment………………………………………………………………………………315\n48．天鹅…………………………………………………………………………………………324\n49．童年的回忆…………………………………………………………………………………324\n50．Green Sleeves………………………………………………………………………………328\n51．绿袖子………………………………………………………………………………… ……332\n52．4分33秒…………………………………………………………………………………336\n53．C大调前奏曲………………………………………………………………………………338\n54．梦想人生……………………………………………………………………………… ……340\n55．秋日私语……………………………………………………………………………………346\n56．勃拉姆斯的摇篮曲…………………………………………………………………………351\n57．献给爱丽丝……………………………………………………………………… …………410\n58．森林波尔卡…………………………………………………………………………………414\n59．天真烂漫……………………………………………………………………………………416\n60．蓝色的爱…………………………………………………………………… ………………417\n61．海边的星空…………………………………………………………………………………363\n62．Night, moon, wind, you…………………………………………………………………367\n63．Lady Di…………………………………………………………………………………368\n64．土耳其进行曲………………………………………………………………………………374\n65．Over the Horizon…………………………………………………………………………382\n66．Tribute…………………………………………………………………………………382\n67．Dance With a Stranger…………………………………………………………………394\n68．Deliverance……………………………………………………………………………398\n69．暑夏清晨…………………………………………………………………… ………………407\n70．克罗地亚狂想曲……………………………………………………………………………414\n71．出埃及记……………………………………………………………………………………422\n72．野蜂飞舞……………………………………………………………… ……………………426\n73．命运交响曲…………………………………………………………………………………432\n74．音乐盒舞者…………………………………………………………………………………438\n75．蜂鸟……………………………………………………………… …………………………443\n76．Wonderland………………………………………………………………………………449\n77．The Ludlows ……………………………………………………………………………460\n78．车尔尼练习曲 Op.740 No.49………………………………………………………………467\n79．少女的祈祷…………………………………………………………………………………474\n80．G大调快板 ………………………………………………………………………………504\n81．君的思恋……………………………………………………… ……………………………503\n82．黄昏之时……………………………………………………………………………………507\n83．Summer…………………………………………………………………………………483\n84．瓦格纳婚礼进行曲…………………………………………… ……………………………520\n85．梁祝…………………………………………………………………………………………530\n86．赛马…………………………………………………………………………………………504\n87．二泉映月………………………………………………… …………………………………509\n88．入殓师………………………………………………………………………………………540\n89．雪之梦………………………………………………………………………………………545\n90．雨的印记…………………………………………… ………………………………………548\n91．River Flows in You………………………………………………………………………526\n92．Time To Love……………………………………………………………………………530\n93．克罗地亚第二狂想曲…………………………… …………………………………………534\n94．门德尔松婚礼进行曲………………………………………………………………………540\n95．思乡病………………………………………………………………………………………547\n96．思乡曲……………………………………… ………………………………………………552\n97．Jardin Secret………………………………………………………………………………557\n98．珊瑚舞………………………………………………………………………………………557\n99．蓝色的多瑙河………………………………………………………………………………561\n100．卡农…………………………………………………………………………………………568"
	xmlPath = "星空·100首云启发音乐总谱.xml"
	label = Label(menu, preOffset = -1, offset = 6)
	label.resolve()
	return EXIT_SUCCESS if label.generate(xmlPath) else EXIT_FAILURE



if __name__ == "__main__":
	exit(main())
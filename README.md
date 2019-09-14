Hero-Skin-Images
======

爬取王者荣耀和英雄联盟的英雄的皮肤图片。

---

Table of Contents
=================

* [爬取王者荣耀英雄皮肤图片](#%E7%88%AC%E5%8F%96%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80%E8%8B%B1%E9%9B%84%E7%9A%AE%E8%82%A4%E5%9B%BE%E7%89%87)
  * [思路分析](#%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90)
  * [涉及到的知识点](#%E6%B6%89%E5%8F%8A%E5%88%B0%E7%9A%84%E7%9F%A5%E8%AF%86%E7%82%B9)
  * [Json数据说明](#json%E6%95%B0%E6%8D%AE%E8%AF%B4%E6%98%8E)
    * [herolist\.json：英雄列表](#herolistjson%E8%8B%B1%E9%9B%84%E5%88%97%E8%A1%A8)
    * [item\.json：英雄装备列表](#itemjson%E8%8B%B1%E9%9B%84%E8%A3%85%E5%A4%87%E5%88%97%E8%A1%A8)
    * [ming\.json：英雄铭文列表](#mingjson%E8%8B%B1%E9%9B%84%E9%93%AD%E6%96%87%E5%88%97%E8%A1%A8)
    * [summoner\.json：召唤师技能列表](#summonerjson%E5%8F%AC%E5%94%A4%E5%B8%88%E6%8A%80%E8%83%BD%E5%88%97%E8%A1%A8)
  * [皮肤图片尺寸分析](#%E7%9A%AE%E8%82%A4%E5%9B%BE%E7%89%87%E5%B0%BA%E5%AF%B8%E5%88%86%E6%9E%90)
  * [程序说明](#%E7%A8%8B%E5%BA%8F%E8%AF%B4%E6%98%8E)
* [爬取英雄联盟英雄皮肤图片](#%E7%88%AC%E5%8F%96%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F%E8%8B%B1%E9%9B%84%E7%9A%AE%E8%82%A4%E5%9B%BE%E7%89%87)
* [License](#license)
* [声明](#%E5%A3%B0%E6%98%8E)

---

## 爬取王者荣耀英雄皮肤图片

### 思路分析

这个项目还是比较简单的，因为很多数据都已经json数据中，我们可以很方便的从中取出我们想要的数据。至于下载皮肤图片的主要难点是拼接图片URL，这里有个小坑就是：每张图片都有5种（或者说至少是5种）尺寸的图片，我之前就只发现了其中一种，当然你可以有选择的进行下载；尺寸详见：[皮肤图片尺寸分析](#%E7%9A%AE%E8%82%A4%E5%9B%BE%E7%89%87%E5%B0%BA%E5%AF%B8%E5%88%86%E6%9E%90)。

### 涉及到的知识点

- 使用json库解析json文件。
- 使用os库创建文件夹。
- 字符串拼接。

### Json数据说明

我已经将可能有用的json文件都下载了，并且进行了格式化（转换编码为utf8）,放在了[`./wzry/json数据/`](<https://github.com/yansheng836/hero-skin-images/tree/master/wzry/json数据>)文件夹下。或者你可以到下面提到的链接中取下载对应的文件（访问json文件URL会自动下载）。



英雄列表介绍主页：<https://pvp.qq.com/web201605/herolist.shtml>，有`herolist.json`。

某个英雄具体介绍主页，如：<https://pvp.qq.com/web201605/herodetail/518.shtml>，有其他三个文件。



#### `herolist.json`：英雄列表

1. 说明：包含英雄id，英雄名，英雄默认皮肤（伴生皮肤：即不用花钱的），英雄类型，英雄皮肤（特指需要花钱买的皮肤，也有可能会在一些活动中会送。**注意**：`skin_name` 这个属性不一定有，比如新英雄可能就没有）。
2. 数据URL : <https://pvp.qq.com/web201605/js/herolist.json>
3. 举例（部分内容）：

```json
[
   {
        "ename": 522,
        "cname": "曜",
        "title": "星辰之子",
        "new_type": 0,
        "hero_type": 1,
        "skin_name": "归虚梦演"
    },
    {
        "ename": 518,
        "cname": "马超",
        "title": "冷晖之枪",
        "new_type": 1,
        "hero_type": 1,
        "hero_type2": 4
    }
]
```

#### `item.json`：英雄装备列表

1. 说明：包含装备id，装备名，装备类型，装备图片id，装备描述。
2. 数据URL : <https://pvp.qq.com/web201605/js/item.json>
3. 举例（部分内容）：

```json
[
      {
        "item_id": 1137,
        "item_name": "暗影战斧",
        "item_type": 1,
        "price": 1254,
        "total_price": 2090,
        "des1": "<p>+85物理攻击<br>+15%冷却缩减<br>+500最大生命</p>",
        "des2": "<p>唯一被动-切割：增加(50+英雄等级*8)点护甲穿透<br>唯一被动-残废：普通攻击有30%几率降低敌人20%移动速度，持续2秒</p>"
    },
    {
        "item_id": 1138,
        "item_name": "破军",
        "item_type": 1,
        "price": 1770,
        "total_price": 2950,
        "des1": "<p>+180物理攻击 </p>",
        "des2": "<p>唯一被动-破军：对生命值低于50%的敌人造成额外30%的伤害</p>"
    }
]
```

#### `ming.json`：英雄铭文列表

1. 说明：包含铭文id，铭文类型，铭文等级，铭文名，铭文描述（属性/加成）。
2. 数据URL : <https://pvp.qq.com/web201605/js/ming.json>
3. 举例（部分内容）：

```json
[
   {
        "ming_id": "1501",
        "ming_type": "red",
        "ming_grade": "5",
        "ming_name": "圣人",
        "ming_des": "<p>法术攻击力+5.3</p>"
    },
    {
        "ming_id": "1503",
        "ming_type": "red",
        "ming_grade": "5",
        "ming_name": "传承",
        "ming_des": "<p>物理攻击力+3.2</p>"
    }
]
```

#### `summoner.json`：召唤师技能列表

1. 说明：（summoner：召唤师（游戏职业名））包含技能id，技能名，召唤师等级（账号达到多少级才能解锁该技能），技能描述。
2. 数据URL : <https://pvp.qq.com/web201605/js/summoner.json>
3. 举例（部分内容）：

```json
[
   {
        "summoner_id": 80104,
        "summoner_name": "惩击",
        "summoner_rank": "LV.1解锁",
        "summoner_description": "30秒CD：对身边的野怪和小兵造成真实伤害并眩晕1秒"
    },
    {
        "summoner_id": 80108,
        "summoner_name": "终结",
        "summoner_rank": "LV.3解锁",
        "summoner_description": "90秒CD：立即对身边敌军英雄造成其已损失生命值14%的真实伤害"
    }
]
```



### 皮肤图片尺寸分析

英雄皮肤图片信息只涉及到 [`herolist.json`](<https://github.com/yansheng836/hero-skin-images/blob/master/wzry/json数据/herolist.json>) 数据，目前发现图片有5种尺寸，注意：下面的图片大小只是对应英雄的图片尺寸，猜测不是固定的，而是在一定范围内变化。

<br/>

下面以英雄马超为例，英雄首页：<https://pvp.qq.com/web201605/herodetail/518.shtml>

| 形式一URL--猜测用于手机端显示                                | 猜测用途         | 图片尺寸 |
| ------------------------------------------------------------ | ---------------- | -------- |
| <https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-smallskin-1.jpg> | 英雄头像         | 67*67    |
| <https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-mobileskin-1.jpg> | 小屏手机英雄背景 | 600*410  |
| <https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-bigskin-1.jpg> | 大屏手机英雄背景 | 1200*530 |

| 形式二URL--猜测是壁纸                                        | 猜测用途 | 图片尺寸 |
| ------------------------------------------------------------ | ---------------- | -------- |
| <https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-mobileskin-1.jpg> | 手机壁纸 | 727*1071 |
| <https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-bigskin-1.jpg> | 电脑壁纸 | 1920*882 |



### 程序说明

1. 测试环境：Python3.7.1，JetBrains PyCharm Community Edition 2018.2.4 x64。

2. 依赖：`requests`，`json`，如果没有安装`requests`，用 `pip install requests` 进行安装即可(`json`为内置库)。

3. 使用说明：主程序为：[`./wzry/wzry.py`](<https://github.com/yansheng836/hero-skin-images/blob/master/wzry/wzry.py>)，运行该程序会将图片下载在当前目录的五个文件夹内，如[`./wzry/phone-bigskin-images/`](<https://github.com/yansheng836/hero-skin-images/tree/master/wzry/phone-bigskin-images>)；如需下载全部英雄图片，请将程序中的[ `break语句`](<https://github.com/yansheng836/hero-skin-images/blob/master/wzry/wzry.py#L153>) 注释掉。



## 爬取英雄联盟英雄皮肤图片

待续。



## License

This work is licensed under a [MIT](https://github.com/yansheng836/hero-skin-images/blob/master/LICENSE.txt).


## 声明

本项目仅用于学习交流使用，**禁止**进行商业目的的开发、发布、运营等。数据所有权归 [腾讯公司](https://www.qq.com/) 所有。
Hero-Skin-Images
======

爬取王者荣耀和英雄联盟的英雄的皮肤图片。

---



## 爬取王者荣耀英雄皮肤图片

### Json数据说明

英雄列表介绍主页：<https://pvp.qq.com/web201605/herolist.shtml>，有herolist.json

某个英雄具体介绍主页：<https://pvp.qq.com/web201605/herodetail/518.shtml>，有其他三个数据。



#### herolist.json：英雄列表

1. 说明：包含英雄id，英雄名，英雄默认皮肤（伴生皮肤：即不用花钱的），英雄类型，英雄皮肤（特指需要花钱买的皮肤，也有可能会在一些活动中会送。**注意**：skin_name这个属性不一定有，比如新英雄可能就没有）。
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

#### item.json：英雄装备列表

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
    },
]
```

#### ming.json：英雄铭文列表

1. 说明：包含铭文id，铭文颜色，铭文等级，铭文名，铭文描述（属性/加成）。
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
    },
]
```

#### summoner.json：召唤师技能列表

1. 说明：（summoner：召唤师（游戏职业名））包含技能id，技能名，账号达到多少级才能解锁该技能，技能描述。
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
    },
]
```



### 皮肤图片

只涉及到herolist.json数据，图片有多重形式。





| 形式一URL--猜测用于手机端显示                                | 猜测用途         | 图片大小 |
| ------------------------------------------------------------ | ---------------- | -------- |
| https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-smallskin-1.jpg | 英雄头像         | 67*67    |
| https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-mobileskin-1.jpg | 小屏手机英雄背景 | 600*410  |
| https://game.gtimg.cn/images/yxzj/img201606/heroimg/518/518-bigskin-1.jpg | 大屏手机英雄背景 | 1200*530 |
| 形式二URL--猜测是壁纸                                        |                  |          |
| https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-mobileskin-1.jpg | 手机壁纸         | 727*1071 |
| https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/518/518-bigskin-1.jpg | 电脑壁纸         | 1920*882 |



创建目录<https://www.cnblogs.com/monsteryang/p/6574550.html>



## 爬取英雄联盟英雄皮肤图片
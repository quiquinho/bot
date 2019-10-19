#!/usr/bin/python
# -*- coding: UTF-8 -*-
import trackingmoreclass
tracker = trackingmoreclass.track
result = ""

#1 List all carriers(列出所有运输商)
# urlStr = ""
# requestData = ""
# result = tracker.trackingmore(requestData, urlStr, "carriers")

#2 detect a carriers by tracking number(识别运输商)
# urlStr = ""
# requestData = "{\"tracking_number\":\"EA152563251CN\"}"
# result = tracker.trackingmore(requestData, urlStr, "carriers/detect")

#3 create a tracking number(新建一个单号)
# urlStr = ""
# requestData = "{\"tracking_number\": \"EA152563242CN\",\"carrier_code\":\"china-post\",\"title\":\"chase chen\",\"customer_name\":\"chase\",\"customer_email\":\"abc@qq.com\",\"order_id\":\"#123\",\"order_create_time\":\"2018-05-20 12:00\",\"destination_code\":\"IL\",\"tracking_ship_date\":\"1521314361\",\"tracking_postal_code\":\"13ES20\",\"lang\":\"en\",\"logistics_channel\":\"4PX page\"}"
# result = tracker.trackingmore(requestData, urlStr, "post")

#4 List all trackings(列出所有跟踪)
#urlStr = "?page=1&limit=100&created_at_min=1521314361&created_at_max=1541314361&update_time_min=1521314361&update_time_max=1541314361&order_created_time_min=1521314361&order_created_time_max=1541314361&numbers=EA152563254CN,UG586285221CN&orders=#123&lang=en"
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "get")

#5 Get tracking results of a single tracking.
# urlStr = "/china-post/RM131516216CN/cn"
# requestData = ""
# result = tracker.trackingmore(requestData, urlStr, "codeNumberGet")

#6 create muti tracking number(创建多个订单号)
#urlStr = ""
#requestData = "[{\"tracking_number\": \"EA152565241CN\",\"carrier_code\":\"china-ems\",\"title\":\"chase chen\",\"customer_name\":\"chase\",\"customer_email\":\"abc@qq.com\",\"order_id\":\"#123444\",\"order_create_time\":\"2018-05-20 12:00\",\"destination_code\":\"IL\",\"tracking_ship_date\":\"1525314361\",\"tracking_postal_code\":\"13ES20\",\"lang\":\"en\",\"logistics_channel\":\"4PX page\"},{\"tracking_number\": \"EA152563242CN\",\"carrier_code\":\"china-ems\",\"title\":\"chase chen\",\"customer_name\":\"chase\",\"customer_email\":\"abc@qq.com\",\"order_id\":\"#123444\",\"order_create_time\":\"2018-05-20 12:00\",\"destination_code\":\"IL\",\"tracking_ship_date\":\"1521314361\",\"tracking_postal_code\":\"13ES20\",\"lang\":\"en\",\"logistics_channel\":\"4PX page1\"}]"
#result = tracker.trackingmore(requestData, urlStr, "batch")

#7 Update Tracking item(更新一个单号)
#urlStr = "/china-ems/EA152565241CN"
#requestData = "{\"title\": \"testtitle\",\"customer_name\":\"python test\",\"customer_email\":\"942632688@qq.com\",\"order_id\":\"#1234567\",\"logistics_channel\":\"chase chen python\",\"customer_phone\":\"+86 13873399982\",\"destination_code\":\"US\",\"status\":\"7\"}"
#result = tracker.trackingmore(requestData, urlStr, "codeNumberPut")

#8 Delete a tracking item(删除一个单号)
#urlStr = "/china-ems/EA152565241CN"
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "codeNumberDelete")

#9 Get realtime tracking results of a single tracking(获取单次跟踪的实时跟踪结果)
#urlStr = ""
#requestData = "{\"tracking_number\": \"61290983300030854514\",\"carrier_code\":\"fedex\",\"destination_code\":\"US\",\"tracking_ship_date\": \"20180226\",\"tracking_postal_code\":\"13ES20\",\"specialNumberDestination\":\"US\",\"order\":\"#123123\",\"order_create_time\":\"2018/3/27 16:51\",\"lang\":\"en\"}"
#result = tracker.trackingmore(requestData, urlStr, "realtime")

#10 Modify courier code(修改运输商)
#urlStr = ""
#requestData = "{\"tracking_number\": \"EA152563242CN\",\"carrier_code\":\"dhl\",\"update_carrier_code\":\"china-ems\"}"
#result = tracker.trackingmore(requestData, urlStr, "update")

#11 Get user info(获取个人信息)
#urlStr = ""
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "getuserinfo")

#12 Get status number(获取单号状态)
#urlStr = ""
#requestData = ""
#result = tracker.trackingmore(requestData, urlStr, "getstatusnumber")

#13 Set number not update(设置单号不再更新)
#urlStr = ""
#requestData = "[{\"tracking_number\":\"LK032051658CN\",\"carrier_code\":\"china-ems\"},{\"tracking_number\":\"EA166023092CN\",\"carrier_code\":\"china-ems\"}]"
#result = tracker.trackingmore(requestData, urlStr, "notupdate")

#14 Get remote iterm results(偏远)
#urlStr = ""
#requestData = "[{\"country\":\"CN\",\"postcode\":\"400422\"},{\"country\":\"CN\",\"postcode\":\"412000\"}]"
#result = tracker.trackingmore(requestData, urlStr, "remote")

#15 Get cost time iterm results(花费时间)
#urlStr = ""
#requestData = "[{\"carrier_code\":\"dhl\",\"destination\":\"US\",\"original\":\"CN\"},{\"carrier_code\":\"dhl\",\"destination\":\"RU\",\"original\":\"CN\"}]"
#result = tracker.trackingmore(requestData, urlStr, "costtime")

#16 Delete multiple tracking item(批量删除)
#urlStr = ""
#requestData = "[{\"tracking_number\":\"EA152563242CN\",\"carrier_code\":\"china-ems\"},{\"tracking_number\":\"EA152563254CN\",\"carrier_code\":\"china-ems\"}]"
#result = tracker.trackingmore(requestData, urlStr, "delete")

#17 Update multiple Tracking item
#urlStr = ""
#requestData = "[{\"tracking_number\":\"RM131516216CN\",\"carrier_code\":\"china-post\",\"title\": \"testtitle\",\"customer_name\":\"python test\",\"customer_email\":\"942632688@qq.com\",\"order_id\":\"#123\",\"logistics_channel\":\"chase chen\",\"destination_code\":\"US\",\"status\":\"7\"},{\"tracking_number\":\"RM111516216CN\",\"carrier_code\":\"china-post\",\"title\": \"testtitle\",\"customer_name\":\"python test\",\"customer_email\":\"942632688@qq.com\",\"order_id\":\"#123\",\"logistics_channel\":\"chase chen\",\"destination_code\":\"US\",\"status\":\"7\"}]"
#result = tracker.trackingmore(requestData, urlStr, "updatemore")



print(result)
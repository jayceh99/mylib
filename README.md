#### my_grafana_api
*****
port 為 8086，使用 HTTP POST


協定文件: 

https://docs.influxdata.com/influxdb/v1.3/guides/writing_data/
https://docs.influxdata.com/influxdb/v1.3/write_protocols/line_protocol_reference/

範例: 

POST /write?consistency=any&db=telegraf_MyDBName HTTP/1.1& 
Host: GrafanaServer:8086
Transfer-Encoding: chunked
Content-Type: text/plain
Accept-Encoding: gzip

2379

disk,path=/,device=sda2,fstype=ext4,host=Server-02 inodes_free=15878859i,inodes_used=308533i,total=260868476928i,free=113815605248i,used=133777899520i,used_percent=54.03126372210472,inodes_total=16187392i 150831397000000000

test,host=Win10 connection=100 910849750580439084

disk,path=/boot/efi,device=sda1,fstype=vfat,host=Server-02 used=3538944i,used_percent=0.6595218466611706,inodes_total=0i,inodes_free=0i,inodes_used=0i,total=536592384i,free=533053440i 150831397000000000

net,interface=em1,host=Server-02 err_in=0i,err_out=0i,bytes_sent=38352053008454i,bytes_recv=43097913890908i,packets_sent=62951152063i,packets_recv=60046845778i,drop_in=1i,drop_out=0i 150831397000000000

說明: 

- 連線 URL

POST db=telegraf_MyDBName

此範例指定將資料寫到 telegraf_MyDBName 資料庫，名稱可自定義，伺服器不會自動建置資料庫

＊資料庫名稱填錯時，監控主機將回傳「database doesn’t exist」

- Post 內容

[TableName,WhereColumnNameList] [SelectKeyValueList] [TimeNanosecond]

disk: from 條件，只能給一個
device=sda2 : where 條件，可多筆用逗號分隔
inodes_free=158788591 : select 條件，填回報值，可多筆用逗號分隔
1508313970000000000 : UTC epoch nanoseconds

WhereColunameNameList: 此範例 host 填入了主機名稱，詳細格式請 line_protocol_reference
*****

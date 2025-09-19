# Student Management Module

## Overview
**Student Management** হলো একটি কাস্টম Odoo অ্যাপ্লিকেশন যা ছাত্রছাত্রী এবং কোর্স ম্যানেজ করার জন্য তৈরি করা হয়েছে।  
এটি ব্যবহার করে আপনি পারবেন:
- ছাত্রছাত্রীদের তথ্য সংরক্ষণ ও ম্যানেজ করতে (নাম, ইমেইল, রোল নাম্বার, ডিপার্টমেন্ট)।  
- কোর্স ডিফাইন করতে (কোর্স কোড, নাম, ক্রেডিট)।  
- একজন ছাত্রছাত্রীকে একাধিক কোর্সে ভর্তি করাতে (many-to-many সম্পর্ক)।  
- কোন ছাত্র কোন কোর্সে ভর্তি আছে, এবং কোন কোর্সে কতজন ছাত্র ভর্তি হয়েছে তা দেখতে।  

---

## Features
- ✅ ইউনিক রোল নাম্বার সহ **স্টুডেন্ট রেকর্ড**  
- ✅ ইউনিক কোর্স কোড সহ **কোর্স রেকর্ড**  
- ✅ স্টুডেন্ট ↔ কোর্স many-to-many সম্পর্ক  
- ✅ ট্রি, ফর্ম এবং সার্চ ভিউ উভয় টেবিলের জন্য  
- ✅ সহজ নেভিগেশন: *Students* এবং *Courses* মেনু থেকে  
- ✅ রিপোর্ট: *কোন কোর্সে কতজন স্টুডেন্ট ভর্তি আছে তা দেখা যায়*  

---

## Steps to Install & Test
1. আপনার Odoo `addons` ফোল্ডারের ভিতরে `student_management` ফোল্ডারটি কপি করুন।  
2. `odoo.conf` ফাইলে `addons_path` এর মধ্যে `student_management` ফোল্ডারটি যুক্ত করুন।  
3. সার্ভার রিস্টার্ট করুন:  
   ```bash
   python odoo-bin -c odoo.conf
4. Odoo-তে লগইন করে Apps মেনুতে যান।

5. Student Management সার্চ করে Install করুন।

6. এখন Student Management → Students / Courses মেনু থেকে ব্যবহার শুরু করতে পারবেন।
---
Challenges & Solutions

❌ Issue: Python version mismatch (Odoo 19 এ Python 3.11 কাজ করছিল না)।
✔ Solution: Lower version (Python 3.10) ব্যবহার করার পর সমস্যার সমাধান হয়েছে।

❌ Issue: কিছু dependency install হচ্ছিল না (যেমন libsass)।
✔ Solution: Microsoft C++ Build Tools install করে সমস্যা সমাধান করা হয়েছে।

❌ Issue: Report view প্রথমে দেখা যাচ্ছিল না।
✔ Solution: আলাদা report ফোল্ডার তৈরি করে XML ফাইলে সঠিকভাবে report ট্যাগ ব্যবহার করেছি।


✍ Author: Jahid
📌 Version: 1.0.0
🛠 Odoo Compatibility: Odoo 19

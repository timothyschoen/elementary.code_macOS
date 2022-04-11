#include <sys/types.h>
#include <sys/select.h>
#include <sys/time.h>
#include <sys/types.h>
#include <errno.h>
#include <stdlib.h>
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>
#include <string.h>

int fd_a; // port descriptor
int nfd; // select() return value
fd_set read_fds;        // file descriptor read flags

struct timeval tv;


void read_pipe(uint8_t* result, int* size) {

    // clear fds read flags
    FD_ZERO(&read_fds);


    // PIPE_A
    FD_SET(fd_a, &read_fds);
    nfd = select(fd_a+1, &read_fds, NULL, NULL, &tv);
    if (nfd != 0) {
        if (nfd == -1) {
            perror("select error");
            return;
        }
        if (FD_ISSET(fd_a, &read_fds)) {

            ssize_t bytes;
            size_t total_bytes = 0;
            char buffer[100*1024];

            while(1) {
              bytes = read(fd_a, buffer + total_bytes, (100*1024 - total_bytes) * sizeof(char));
              if (bytes > 0) {
                  total_bytes += (size_t)bytes;
              }
              else {
                strncpy(result, buffer, total_bytes);
                (*size) = (int)total_bytes;
                break;
              }
            }
        }
    }
}

void start_listening() {

      tv.tv_sec = 0;
      tv.tv_usec = 10000;

      system("mkfifo /tmp/PIPE_ELEMENTARY_CODE");
      system("chmod 666 /tmp/PIPE_*");
      fd_a = open("/tmp/PIPE_ELEMENTARY_CODE", O_RDONLY | O_NONBLOCK);
}

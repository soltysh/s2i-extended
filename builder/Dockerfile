# We are basing our builder image on one of openshift's existing builder images.
# Here, it is the latest available python image, at the time
FROM centos/python-35-centos7

# Switch to root user to be able to install packages
USER 0

# Enable EPEL repository & install freetds-devel drivers to access MSSQL server
RUN yum install -y epel-release && \
    yum install -y freetds-devel && \
    yum clean all -y

# Switch back to a non-privileged user
USER 1001

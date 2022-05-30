
#!/bin/bash

DOCKER_FILE=$1
LOG_DIR=/home/user/deploy_logs/bfc/
LOG_FILE=${LOG_DIR}deploy.log
FRONTEND_BRANCH=Frontend_Develop
FRONTEND_PATH=/home/user/bfc-frontend/
BACKEND_BRANCH=Backend_Develop
BACKEND_PATH=/home/user/bfc-backend-dev/
echo $LOG_FILE
mkdir -p $LOG_DIR


# shellcheck disable=SC2120
deploy_frontend() {
  cd $FRONTEND_PATH

  git remote update
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "origin/$FRONTEND_BRANCH")
  BASE=$(git merge-base @ "origin/$FRONTEND_BRANCH")
  if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
  elif [ $LOCAL = $BASE ]; then

        git pull origin $FRONTEND_BRANCH

        echo "Deploying Frontend!"
        docker-compose build &gt;&gt; "$LOG_FILE" 2&gt;&amp;1

        cd $BACKEND_PATH

        if [ "$DOCKER_FILE" ]; then
          docker-compose -f "$DOCKER_FILE" build nginx &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
          docker-compose -f "$DOCKER_FILE" up -d nginx &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
        else
          docker-compose build nginx &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
          docker-compose up -d nginx &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
        fi

        if [ $? -eq 0 ]
        then
            echo "Deployment success"
        else
            echo "Deployment failure"
        fi
  elif [ $REMOTE = $BASE ]; then
      echo "Need to push"
  else
      echo "Diverged"
  fi
}

# shellcheck disable=SC2120
deploy_backend() {
  cd $BACKEND_PATH

  git remote update
  LOCAL=$(git rev-parse @)
  REMOTE=$(git rev-parse "origin/$BACKEND_BRANCH")
  BASE=$(git merge-base @ "origin/$BACKEND_BRANCH")
  if [ $LOCAL = $REMOTE ]; then
    echo "Up-to-date"
  elif [ $LOCAL = $BASE ]; then
      git pull origin $BACKEND_BRANCH

      echo "Deploying Backend!"
      if [ "$DOCKER_FILE" ]; then
        docker-compose -f "$DOCKER_FILE" build admin dock iam &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
        docker-compose -f "$DOCKER_FILE" up -d admin dock iam&gt;&gt; "$LOG_FILE" 2&gt;&amp;1
      else
        docker-compose build admin dock iam &gt;&gt; "$LOG_FILE" 2&gt;&amp;1
        docker-compose up -d admin dock iam&gt;&gt; "$LOG_FILE" 2&gt;&amp;1
      fi
      if [ $? -eq 0 ]
      then
          echo "Deployment success"
      else
          echo "Deployment failure"
      fi
  elif [ $REMOTE = $BASE ]; then
      echo "Need to push"
  else
      echo "Diverged"
  fi
}

case "$2" in
  -f) echo "Frontend deployment starting..."
    deploy_frontend
  ;;
  -b) echo "Backend deployment starting..."
    deploy_backend
    ;;
  *)
    echo "Usage : $0 docker-compose.yml -f -b"
    exit
    ;;
esac

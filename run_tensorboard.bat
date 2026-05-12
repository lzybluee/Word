python -m pip list | find "tensorboard"
if %errorlevel% neq 0 (
    python -m pip install tensorboard
)

start /b python -m tensorboard.main --logdir oss_data --port 6006 --bind_all

:loop
sleep 2
netstat -an | find "0.0.0.0:6006"
if %errorlevel% == 0 (
    goto end
) else (
    goto loop
)
:end

start "" "http://localhost:6006#projector"

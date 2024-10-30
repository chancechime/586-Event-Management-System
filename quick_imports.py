from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_session import Session
import webbrowser
import os
from AWS import AWS
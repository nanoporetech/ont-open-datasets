/**
 * Bio component that queries for data
 * with Gatsby's useStaticQuery component
 *
 * See: https://www.gatsbyjs.org/docs/use-static-query/
 */

import React from "react"
import {graphql, useStaticQuery, Link} from "gatsby";
import logo from '../../../content/assets/ont-logo.svg';
import styles from './navBar.module.css'

const NavBar = () => {

  const data = useStaticQuery(graphql`
    query NavBarQuery {
      site {
        siteMetadata {
          author {
            name
          }
        }
      }
    }
  `);

  // Set these values by editing "siteMetadata" in gatsby-config.js
  const author = data.site.siteMetadata?.author;

  return (
    <div className={styles.navBar}>
      <div className={styles.navBarLogo}>
        <img
          src={logo}
          alt={author?.name || ``}
        />
      </div>

      <div className={styles.navBarLinks}>
        <ul>
          <li>
            <Link to="/about/">
              About
            </Link>
          </li>
        </ul>
      </div>
    </div>
)};

export default NavBar
